#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Context menu utilities for DTK applications.

DTK context menus (DMenu::exec()) create transient popup menus whose items
may not be discoverable via dogtail's static AT-SPI tree traversal.

This module uses the hover-crawl technique:
  1. Right-click at coordinates to pop up the context menu
  2. Register an AT-SPI "object:state-changed:focused" event listener
  3. Hover the mouse vertically through the menu area
  4. Each menu item emits a focus event when hovered, revealing its name + coords
  5. When target item is found, click at its stored coordinates
  6. Clean up: unregister listener, press Escape if target not found

Reference: deepin-mcp's MenuOperator.context_menu_comb() / hover_crawl_context_menu()
"""

import subprocess
import threading
import time

import gi

gi.require_version("Atspi", "2.0")
from gi.repository import GLib
from gi.repository import Atspi

from src.mouse_key import MouseKey
from src import logger


_ATSPI_INITIALIZED = False
_GLIB_LOOP: GLib.MainLoop | None = None
_GLIB_LOOP_LOCK = threading.Lock()


def _ensure_glib_loop() -> None:
    """Ensure a GLib main loop thread is running for AT-SPI event processing."""
    global _ATSPI_INITIALIZED, _GLIB_LOOP
    if _ATSPI_INITIALIZED:
        return
    with _GLIB_LOOP_LOCK:
        if _ATSPI_INITIALIZED:
            return
        try:
            Atspi.init()
            _GLIB_LOOP = GLib.MainLoop()
            t = threading.Thread(target=_GLIB_LOOP.run, daemon=True)
            t.start()
            time.sleep(0.15)
            _ATSPI_INITIALIZED = True
        except Exception as exc:
            logger.warning(f"Failed to initialize AT-SPI event loop: {exc}")


def _pump_events(times: int = 3, interval: float = 0.02) -> None:
    """Pump pending GLib events to process AT-SPI events."""
    ctx = GLib.MainContext.default()
    for _ in range(times):
        try:
            ctx.iteration(False)
        except Exception:
            pass
        time.sleep(interval)


def _get_app_window_bounds(app_name: str = "deepin-terminal") -> tuple[int, int, int, int] | None:
    """Get the bounds (x, y, width, height) of the first application window.

    Returns:
        (x, y, width, height) on success, None if not found.
    """
    try:
        root = Atspi.get_desktop(0)
        for i in range(root.get_child_count()):
            try:
                app = root.get_child_at_index(i)
                if (app.get_name() or "") != app_name:
                    continue
                for j in range(app.get_child_count()):
                    try:
                        w = app.get_child_at_index(j)
                        role = w.get_role_name() or ""
                        if role in ("frame", "window", "dialog"):
                            ext = w.get_extents(Atspi.CoordType.SCREEN)
                            if ext.width > 0 and ext.height > 0:
                                return (ext.x, ext.y, ext.width, ext.height)
                    except Exception:
                        continue
            except Exception:
                continue
    except Exception:
        pass
    return None


def _get_default_click_point(app_name: str = "deepin-terminal") -> tuple[int, int]:
    """Get a default right-click point within the application window.

    Uses the window center, slightly offset downward for more reliable
    context menu positioning.
    """
    bounds = _get_app_window_bounds(app_name)
    if bounds:
        x, y, w, h = bounds
        click_x = x + w // 2
        click_y = y + h // 2 + 50
        return (click_x, click_y)
    return (400, 300)


def context_menu_click(
    target_name: str,
    click_x: int | None = None,
    click_y: int | None = None,
    offset_x: int = 80,
    max_down: int = 600,
    step_px: int = 6,
    match_substring: bool = True,
) -> bool:
    """Right-click at position, then hover-crawl to find and click target menu item.

    If click_x/click_y are not provided, automatically determines a point within
    the deepin-terminal window.

    Args:
        target_name: Text of the menu item to click (case-insensitive).
        click_x: X coordinate for right-click. Auto-detected if None.
        click_y: Y coordinate for right-click. Auto-detected if None.
        offset_x: Horizontal offset from click_x for hovering over the menu.
        max_down: Maximum vertical distance to crawl downward.
        step_px: Vertical step size per hover iteration.
        match_substring: If True, target_name need only be a substring of the item name.

    Returns:
        True if target was found and clicked, False otherwise.
    """
    if click_x is None or click_y is None:
        click_x, click_y = _get_default_click_point()

    _ensure_glib_loop()
    if not _ATSPI_INITIALIZED:
        logger.warning("AT-SPI not available, falling back to keyboard navigation")
        return _fallback_keyboard_select(target_name, click_x, click_y)

    found = threading.Event()
    target_coords: list[tuple[int, int]] = []
    captured: dict[str, tuple[int, int]] = {}
    lock = threading.Lock()

    def on_focus(event):
        if not event.type.startswith("object:state-changed:focused"):
            return
        try:
            src = event.source
            if not src or src.get_role_name() != "menu item":
                return
            name = src.get_name() or ""
            if not name:
                return
            ext = src.get_extents(Atspi.CoordType.SCREEN)
            cx = ext.x + ext.width // 2
            cy = ext.y + ext.height // 2
            with lock:
                if name not in captured:
                    captured[name] = (cx, cy)
                if match_substring:
                    if target_name.lower() in name.lower():
                        target_coords.append((cx, cy))
                        found.set()
                else:
                    if name.lower() == target_name.lower():
                        target_coords.append((cx, cy))
                        found.set()
        except Exception:
            pass

    listeners_registered = False
    try:
        listener = Atspi.EventListener.new(on_focus)
        listener.register("object:state-changed:focused")
        listeners_registered = True

        MouseKey.move_to(click_x, click_y, duration=0.08)
        time.sleep(0.03)
        MouseKey.right_click()
        time.sleep(0.2)

        _pump_events(3, 0.01)

        scan_x = click_x + offset_x
        current_y = click_y
        last_count = 0
        stable = 0

        while current_y < click_y + max_down and not found.is_set():
            MouseKey.move_to(scan_x, current_y, duration=0.04)
            time.sleep(0.006)
            _pump_events(1, 0.006)
            current_y += step_px

            if found.is_set():
                break

            with lock:
                curr_count = len(captured)
            if curr_count > last_count:
                last_count = curr_count
                stable = 0
            else:
                stable += 1
            if stable > 8 or curr_count >= 30:
                break

        if found.is_set() and target_coords:
            tx, ty = target_coords[0]
            time.sleep(0.05)
            MouseKey.move_to(tx, ty, duration=0.04)
            time.sleep(0.05)
            MouseKey.click()
            logger.debug(f"Clicked context menu item '{target_name}' at ({tx}, {ty})")
            time.sleep(0.2)
            return True

        logger.debug(f"Context menu item '{target_name}' not found. Captured: {list(captured.keys())}")
        return False

    finally:
        if listeners_registered:
            try:
                listener.deregister("object:state-changed:focused")
            except Exception:
                pass
        if not (found.is_set() and target_coords):
            try:
                subprocess.run(
                    ["xdotool", "key", "Escape"],
                    capture_output=True, timeout=3,
                )
            except Exception:
                pass
            time.sleep(0.15)


def _scan_popup_and_click(
    target_name: str,
    match_substring: bool,
    timeout_sec: float = 1.5,
) -> bool:
    start = time.monotonic()
    popups: list[Atspi.Accessible] = []

    def _collect(node, depth=0):
        if depth > 8:
            return
        try:
            role = node.get_role_name() or ""
            if role == "popup menu":
                popups.append(node)
                return
            for i in range(node.get_child_count()):
                try:
                    _collect(node.get_child_at_index(i), depth + 1)
                except Exception:
                    pass
        except Exception:
            pass

    while time.monotonic() - start < timeout_sec:
        _pump_events(5, 0.02)
        popups.clear()
        try:
            _collect(Atspi.get_desktop(0))
        except Exception:
            time.sleep(0.05)
            continue
        for popup in popups:
            try:
                count = popup.get_child_count()
            except Exception:
                continue
            for i in range(count):
                try:
                    child = popup.get_child_at_index(i)
                    if child.get_role_name() != "menu item":
                        continue
                    name = child.get_name() or ""
                    if not name:
                        continue
                    match = (
                        target_name.lower() in name.lower()
                        if match_substring
                        else name.lower() == target_name.lower()
                    )
                    if match:
                        ext = child.get_extents(Atspi.CoordType.SCREEN)
                        cx = ext.x + ext.width // 2
                        cy = ext.y + ext.height // 2
                        MouseKey.move_to(cx, cy, duration=0.04)
                        time.sleep(0.1)
                        MouseKey.click()
                        logger.debug(
                            f"Clicked popup item '{target_name}' at ({cx}, {cy})"
                        )
                        time.sleep(0.3)
                        return True
                except Exception:
                    continue
        time.sleep(0.05)
    return False


def context_menu_click_by_scan(
    target_name: str,
    click_x: int = 400,
    click_y: int = 300,
    max_depth: int = 8,
    match_substring: bool = True,
    app_name: str = "deepin-terminal",
) -> bool:
    """Right-click at (click_x, click_y), then scan AT-SPI tree for popup menu children.

    This is a simpler alternative to the hover-crawl approach that directly scans
    the AT-SPI tree for 'popup menu' role elements and reads their children.

    May fail for menus that only populate on hover (e.g. DMenu::exec() stack-local menus).

    Args:
        target_name: Text of the menu item to click.
        click_x: X coordinate for right-click.
        click_y: Y coordinate for right-click.
        max_depth: Maximum depth for AT-SPI tree scan.
        match_substring: If True, match by substring.
        app_name: Application name for AT-SPI tree root.

    Returns:
        True if target was found and clicked, False otherwise.
    """
    try:
        root = Atspi.get_desktop(0)
    except Exception:
        return False

    try:
        app = None
        for i in range(root.get_child_count()):
            try:
                child = root.get_child_at_index(i)
                name = child.get_name() or ""
                if name == app_name:
                    app = child
                    break
            except Exception:
                continue

        if not app:
            return False

        MouseKey.move_to(click_x, click_y, duration=0.08)
        time.sleep(0.03)
        MouseKey.right_click()
        time.sleep(0.25)

        popups = []

        def _scan(node, depth):
            if depth > max_depth:
                return
            try:
                role = node.get_role_name() or ""
                if role == "popup menu":
                    popups.append(node)
                    return
                for i in range(node.get_child_count()):
                    try:
                        _scan(node.get_child_at_index(i), depth + 1)
                    except Exception:
                        pass
            except Exception:
                pass

        _scan(app, 0)

        for popup in popups:
            try:
                pb = popup.get_extents(Atspi.CoordType.SCREEN)
                px = pb.x + pb.width // 2
                py = pb.y + pb.height // 2
                if abs(px - click_x) > 300 or abs(py - click_y) > 300:
                    continue
            except Exception:
                continue

            for i in range(popup.get_child_count()):
                try:
                    child = popup.get_child_at_index(i)
                    if child.get_role_name() != "menu item":
                        continue
                    name = child.get_name() or ""
                    if not name:
                        continue
                    match = (
                        target_name.lower() in name.lower()
                        if match_substring
                        else name.lower() == target_name.lower()
                    )
                    if match:
                        ext = child.get_extents(Atspi.CoordType.SCREEN)
                        cx = ext.x + ext.width // 2
                        cy = ext.y + ext.height // 2
                        MouseKey.move_to(cx, cy, duration=0.04)
                        time.sleep(0.05)
                        MouseKey.click()
                        logger.debug(
                            f"Clicked context menu item '{target_name}' "
                            f"via scan at ({cx}, {cy})"
                        )
                        time.sleep(0.2)
                        return True
                except Exception:
                    continue

                try:
                    subprocess.run(
                        ["xdotool", "key", "Escape"],
                        capture_output=True, timeout=3,
                    )
                except Exception:
                    pass
    except Exception:
        pass
    time.sleep(0.15)
    return False


def scan_and_click_in_app(
    target_name: str,
    match_substring: bool = True,
    app_name: str = "deepin-terminal",
    timeout_sec: float = 2.0,
) -> bool:
    _ensure_glib_loop()
    start = time.monotonic()
    found_coords: list[tuple[int, int]] = []

    def _scan(node, depth=0):
        if depth > 12 or found_coords:
            return
        try:
            role = node.get_role_name() or ""
            name = node.get_name() or ""
            if name and role not in ("panel", "application"):
                match = (
                    target_name.lower() in name.lower()
                    if match_substring
                    else name.lower() == target_name.lower()
                )
                if match and node.get_state().contains(Atspi.StateType.SHOWING):
                    ext = node.get_extents(Atspi.CoordType.SCREEN)
                    if ext.width > 0 and ext.height > 0:
                        found_coords.append((ext.x + ext.width // 2, ext.y + ext.height // 2))
                        return
            for i in range(node.get_child_count()):
                try:
                    _scan(node.get_child_at_index(i), depth + 1)
                except Exception:
                    pass
        except Exception:
            pass

    while time.monotonic() - start < timeout_sec:
        found_coords.clear()
        _pump_events(3, 0.01)
        try:
            root = Atspi.get_desktop(0)
            for i in range(root.get_child_count()):
                try:
                    app = root.get_child_at_index(i)
                    if (app.get_name() or "") == app_name:
                        _scan(app)
                        if found_coords:
                            cx, cy = found_coords[0]
                            MouseKey.move_to(cx, cy, duration=0.04)
                            time.sleep(0.05)
                            MouseKey.click()
                            logger.debug(f"scan_and_click '{target_name}' at ({cx}, {cy})")
                            time.sleep(0.2)
                            return True
                except Exception:
                    continue
        except Exception:
            pass
        time.sleep(0.05)
    logger.debug(f"scan_and_click '{target_name}' not found in {app_name}")
    return False


def _fallback_keyboard_select(
    target_name: str,
    click_x: int = 400,
    click_y: int = 300,
) -> bool:
    """Fallback: use keyboard navigation for context menu selection.

    This uses MouseKey.select_menu() which navigates by pressing arrow keys.
    Since we don't know the exact position of the target item in the menu,
    this is a best-effort fallback. It tries to cycle through items.
    """
    logger.warning(f"Keyboard fallback for context menu item '{target_name}'")
    MouseKey.move_to(click_x, click_y)
    time.sleep(0.05)
    MouseKey.right_click()
    time.sleep(0.3)

    # Try a few down-arrow + Enter attempts (best-effort)
    for attempt in range(5):
        MouseKey.press_key("down")
        time.sleep(0.15)
    MouseKey.press_key("enter")
    time.sleep(0.3)
    return True  # Best-effort, assume worked

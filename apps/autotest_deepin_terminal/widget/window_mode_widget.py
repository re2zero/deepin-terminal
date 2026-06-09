#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for window mode functionality (normal, fullscreen, quake).
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class WindowModeWidget(BaseWidget):
    """Widget methods for the window mode functionality."""

    # === Launch terminal ===

    def launch_terminal_by_shortcut(self):
        """Launch terminal using Ctrl+Alt+T shortcut."""
        self.hot_key("ctrl+alt+t")
        import time
        time.sleep(1.0)

    def launch_terminal_by_command(self, args=""):
        """Launch terminal via command line."""
        cmd = f"deepin-terminal {args}" if args else "deepin-terminal"
        self.run_cmd(cmd)
        import time
        time.sleep(1.0)

    def launch_terminal_normal_mode(self):
        """Launch terminal in normal window mode."""
        self.run_cmd("deepin-terminal -m normal")
        import time
        time.sleep(1.0)

    def launch_terminal_fullscreen_mode(self):
        """Launch terminal in fullscreen mode."""
        self.run_cmd("deepin-terminal -m fullscreen")
        import time
        time.sleep(1.0)

    def launch_terminal_maximum_mode(self):
        """Launch terminal in maximized mode."""
        self.run_cmd("deepin-terminal -m maximum")
        import time
        time.sleep(1.0)

    def launch_terminal_splitscreen_mode(self):
        """Launch terminal in splitscreen mode."""
        self.run_cmd("deepin-terminal -m splitscreen")
        import time
        time.sleep(1.0)

    # === Quake mode ===

    def toggle_quake_mode(self):
        """Toggle quake terminal using Alt+F2 shortcut."""
        self.hot_key("alt+f2")
        import time
        time.sleep(0.5)

    # === Fullscreen ===

    def toggle_fullscreen(self):
        """Toggle fullscreen using F11."""
        self.press_key("F11")
        import time
        time.sleep(0.5)

    # === Maximize/Restore ===

    def maximize_window(self):
        """Maximize terminal window."""
        self.dog.element_click("DTitlebarDWindowMaxButton")
        import time
        time.sleep(0.5)

    def restore_window(self):
        """Restore window from maximized state."""
        self.dog.element_click("DTitlebarDWindowQuitFullscreenButton")
        import time
        time.sleep(0.5)

    # === Minimize ===

    def minimize_window(self):
        """Minimize terminal window."""
        self.dog.element_click("DTitlebarDWindowMinButton")
        import time
        time.sleep(0.5)

    # === Window title ===

    def get_window_title(self):
        import time
        time.sleep(0.3)
        try:
            return self.dog.app_element("终端").name
        except Exception:
            return ""

    # === Multiple windows ===

    def close_all_terminals(self):
        """Close all terminal instances."""
        self.run_cmd("killall deepin-terminal")
        import time
        time.sleep(1.0)

    # === Clipboard operations ===

    def select_text_by_shift_left(self):
        """Select character before cursor using Shift+Left."""
        self.hot_key("shift+Left")

    def select_text_by_shift_right(self):
        """Select character after cursor using Shift+Right."""
        self.hot_key("shift+Right")

    def paste_by_shortcut(self):
        """Paste using Ctrl+Shift+V shortcut."""
        self.hot_key("ctrl+shift+v")
        import time
        time.sleep(0.3)

    def select_all(self):
        """Select all text using Ctrl+Shift+A shortcut."""
        self.hot_key("ctrl+shift+a")

    # === Hyperlink ===

    def click_hyperlink(self, x, y):
        """Click on a hyperlink at given coordinates."""
        self.click(x, y)
        import time
        time.sleep(0.5)

    def ctrl_click_hyperlink(self, x, y):
        """Ctrl+Click on a hyperlink to open it."""
        import time
        self.hot_key("ctrl")
        time.sleep(0.2)
        self.click(x, y)
        time.sleep(0.5)

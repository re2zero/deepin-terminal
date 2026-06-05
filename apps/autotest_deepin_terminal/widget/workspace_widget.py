#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for workspace (tab/split) functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class WorkspaceWidget(BaseWidget):
    """Widget methods for the workspace functionality."""

    # === Tab operations ===

    def new_tab_by_plus_button(self):
        """Click the + button to create a new tab."""
        self.dog.element_click("DTabBarAddButton")

    def new_tab_by_shortcut(self):
        """Create a new tab using Ctrl+Shift+T shortcut."""
        self.hot_key("ctrl+shift+t")

    def close_current_tab(self):
        """Close current tab using Alt+W shortcut."""
        self.hot_key("alt+w")

    def close_current_tab_by_shortcut_setting(self):
        """Close current tab using configured shortcut (default alt+w)."""
        self.hot_key("alt+w")

    def switch_to_tab_by_index(self, index):
        """Switch to tab by index using Ctrl+Shift+<index>."""
        self.hot_key(f"ctrl+shift+{index}")

    def switch_tab_forward(self):
        """Switch to next tab using Ctrl+Tab."""
        self.hot_key("ctrl+tab")

    def switch_tab_backward(self):
        """Switch to previous tab using Ctrl+Shift+Tab."""
        self.hot_key("ctrl+shift+tab")

    # === Split operations ===

    def horizontal_split_by_menu(self):
        """Create horizontal split via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("横向分屏")
        time.sleep(0.5)

    def vertical_split_by_menu(self):
        """Create vertical split via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("纵向分屏")
        time.sleep(0.5)

    def horizontal_split_by_shortcut(self):
        """Create horizontal split using Ctrl+Shift+H shortcut."""
        self.hot_key("ctrl+shift+h")

    def vertical_split_by_shortcut(self):
        """Create vertical split using Ctrl+Shift+J shortcut."""
        self.hot_key("ctrl+shift+j")

    def close_workspace_by_shortcut(self):
        """Close current workspace using Alt+Q shortcut."""
        self.hot_key("alt+q")

    def select_upper_workspace(self):
        """Select upper workspace using Alt+Up shortcut."""
        self.hot_key("alt+up")

    def select_lower_workspace(self):
        """Select lower workspace using Alt+Down shortcut."""
        self.hot_key("alt+down")

    # === Tab right-click menu ===

    def right_click_tab(self):
        """Right-click on the current tab."""
        import time
        self.dog.element_right_click("工作区")

    def close_tab_from_context_menu(self):
        """Close tab via tab right-click context menu."""
        self.right_click_tab()
        import time
        time.sleep(0.3)
        self.dog.element_click("关闭标签页")
        time.sleep(0.3)

    def close_other_tabs_from_context_menu(self):
        """Close other tabs via tab right-click context menu."""
        self.right_click_tab()
        import time
        time.sleep(0.3)
        self.dog.element_click("关闭其它标签页")
        time.sleep(0.3)

    def rename_tab_from_context_menu(self):
        """Rename tab title via tab right-click context menu."""
        self.right_click_tab()
        import time
        time.sleep(0.3)
        self.dog.element_click("重命名标题")
        time.sleep(0.3)

    # === Window operations ===

    def fullscreen_by_menu(self):
        """Toggle fullscreen via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("全屏")
        time.sleep(0.5)

    def fullscreen_by_shortcut(self):
        """Toggle fullscreen using F11 shortcut."""
        self.press_key("F11")

    def exit_fullscreen(self):
        """Exit fullscreen mode."""
        self.dog.element_click("退出全屏")
        import time
        time.sleep(0.5)

    # === Scrollbar ===

    def scroll_page_down(self):
        """Scroll page down using Shift+PageDown."""
        self.hot_key("shift+next")

    def scroll_page_up(self):
        """Scroll page up using Shift+PageUp."""
        self.hot_key("shift+prior")

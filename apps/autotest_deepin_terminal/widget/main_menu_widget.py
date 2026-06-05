#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for main menu bar and window controls.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class MainMenuWidget(BaseWidget):
    """Widget methods for the main menu bar functionality."""

    # === Main menu ===

    def click_main_menu(self):
        """Click the main menu button."""
        self.dog.element_click("DTitlebarDWindowOptionButton")
        import time
        time.sleep(0.3)

    def close_main_menu_by_esc(self):
        """Close main menu by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    def navigate_menu_by_arrow_keys(self):
        """Navigate menu items using arrow keys."""
        import time
        self.press_key("Down")
        time.sleep(0.2)
        self.press_key("Up")
        time.sleep(0.2)

    def select_menu_item(self, item_name):
        """Select and click a menu item."""
        self.dog.element_click(item_name)
        import time
        time.sleep(0.5)

    def expand_submenu(self):
        """Expand submenu by pressing Right arrow or Enter."""
        self.press_key("Right")
        import time
        time.sleep(0.3)

    def collapse_submenu(self):
        """Collapse submenu by pressing Left arrow."""
        self.press_key("Left")
        import time
        time.sleep(0.3)

    # === Theme ===

    def switch_theme_dark(self):
        """Switch to dark theme via main menu."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("主题")
        time.sleep(0.3)
        self.dog.element_click("深色")
        time.sleep(0.5)

    def switch_theme_light(self):
        """Switch to light theme via main menu."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("主题")
        time.sleep(0.3)
        self.dog.element_click("浅色")
        time.sleep(0.5)

    def switch_theme_system(self):
        """Switch to follow system theme via main menu."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("主题")
        time.sleep(0.3)
        self.dog.element_click("跟随系统")
        time.sleep(0.5)

    # === Help ===

    def click_help(self):
        """Click Help menu item."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("帮助")
        import time
        time.sleep(0.5)

    def open_help_by_f1(self):
        """Open help using F1 key."""
        self.press_key("F1")
        import time
        time.sleep(0.5)

    # === About ===

    def click_about(self):
        """Click About menu item."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("关于")
        import time
        time.sleep(0.5)

    def close_about_by_x(self):
        """Close about dialog by clicking X button."""
        self.dog.element_click("DTitlebarDWindowCloseButton")
        import time
        time.sleep(0.3)

    def close_about_by_esc(self):
        """Close about dialog by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    def close_about_by_alt_f4(self):
        """Close about dialog by pressing Alt+F4."""
        self.hot_key("alt+F4")
        import time
        time.sleep(0.3)

    # === Settings (via menu) ===

    def click_settings(self):
        """Click Settings menu item."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("设置")
        import time
        time.sleep(0.5)

    # === Exit ===

    def click_exit(self):
        """Click Exit menu item."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("退出")
        import time
        time.sleep(0.5)

    # === Window controls ===

    def click_minimize(self):
        """Click minimize button."""
        self.dog.element_click("DTitlebarDWindowMinButton")
        import time
        time.sleep(0.5)

    def click_maximize(self):
        """Click maximize button."""
        self.dog.element_click("DTitlebarDWindowMaxButton")
        import time
        time.sleep(0.5)

    def click_restore(self):
        """Click restore button (when maximized)."""
        self.dog.element_click("DTitlebarDWindowQuitFullscreenButton")
        import time
        time.sleep(0.5)

    def click_close(self):
        """Click close button."""
        self.dog.element_click("DTitlebarDWindowCloseButton")
        import time
        time.sleep(0.5)

    # === New window ===

    def click_new_window(self):
        """Click 'New window' from main menu."""
        self.click_main_menu()
        import time
        time.sleep(0.3)
        self.dog.element_click("新建窗口")
        import time
        time.sleep(0.5)

    # === Keyboard shortcut display ===

    def show_shortcut_help(self):
        """Show shortcut help using Ctrl+Shift+?."""
        self.hot_key("ctrl+shift+?")
        import time
        time.sleep(0.3)

    # === Tab navigation ===

    def tab_to_main_menu(self):
        """Tab to main menu button from terminal."""
        import time
        # Use Super+Tab to jump to tab bar area
        self.hot_key("Super_L,Tab")
        time.sleep(0.3)

    def tab_to_minimize(self):
        """Tab to minimize button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    def tab_to_close(self):
        """Tab to close button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

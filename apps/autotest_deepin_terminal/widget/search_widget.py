#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for search/find functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class SearchWidget(BaseWidget):
    """Widget methods for the search functionality."""

    # === Open search ===

    def open_search_by_menu(self):
        """Open search bar via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("查找")
        time.sleep(0.5)

    def open_search_by_shortcut(self):
        """Open search bar using Ctrl+Alt+F shortcut."""
        self.hot_key("ctrl+alt+f")
        import time
        time.sleep(0.5)

    # === Search operations ===

    def input_search_text(self, text):
        """Type search text into the search input box."""
        self.input_message(text)
        import time
        time.sleep(0.3)

    def search_forward(self):
        """Search forward (downward) by pressing Enter."""
        self.press_key("Return")
        import time
        time.sleep(0.3)

    def search_backward(self):
        """Search backward (upward) by pressing Shift+Enter."""
        self.hot_key("shift+Return")
        import time
        time.sleep(0.3)

    def click_search_up_button(self):
        """Click the search upward button."""
        self.dog.element_click("向上搜索")

    def click_search_down_button(self):
        """Click the search downward button."""
        self.dog.element_click("向下搜索")

    def clear_search_by_x(self):
        """Clear search input by clicking the X button."""
        self.dog.element_click("DTitlebarDWindowCloseButton")

    # === Close search ===

    def close_search_by_esc(self):
        """Close search bar by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    def close_search_by_click(self):
        """Close search bar by clicking elsewhere in terminal."""
        self.click(400, 400)
        import time
        time.sleep(0.3)

    # === Tab navigation in search bar ===

    def tab_to_search_down(self):
        """Tab to search downward button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    def tab_to_search_up(self):
        """Tab to search upward button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

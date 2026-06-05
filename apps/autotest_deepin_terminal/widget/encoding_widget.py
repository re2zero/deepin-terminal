#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for encoding functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class EncodingWidget(BaseWidget):
    """Widget methods for the encoding functionality."""

    # === Open encoding panel ===

    def open_encoding_by_menu(self):
        """Open encoding panel via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("编码")
        time.sleep(0.5)

    def open_encoding_by_alt_m(self):
        """Open encoding panel via Alt+M menu."""
        self.hot_key("alt+m")
        import time
        time.sleep(0.3)
        self.dog.element_click("编码")
        time.sleep(0.5)

    # === Encoding operations ===

    def select_encoding(self, encoding_name):
        """Select a specific encoding from the encoding list."""
        self.dog.element_click(encoding_name)
        import time
        time.sleep(0.5)

    def is_encoding_panel_visible(self):
        """Check if encoding panel is visible."""
        return self.dog.is_element_exist("编码")

    def hide_encoding_by_click(self):
        """Hide encoding panel by clicking on terminal area."""
        self.click(400, 400)
        import time
        time.sleep(0.3)

    def hide_encoding_by_double_click(self):
        """Hide encoding panel by double-clicking on terminal area."""
        self.double_click(400, 400)
        import time
        time.sleep(0.3)

    def hide_encoding_by_esc(self):
        """Hide encoding panel by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    # === Keyboard navigation in encoding panel ===

    def navigate_encoding_by_arrow_keys(self):
        """Navigate encoding list using arrow keys."""
        import time
        self.press_key("Down")
        time.sleep(0.3)
        self.press_key("Up")
        time.sleep(0.3)

    def select_encoding_by_enter(self):
        """Confirm encoding selection by pressing Enter."""
        self.press_key("Return")
        import time
        time.sleep(0.5)

    def hide_encoding_by_tab(self):
        """Switch focus from encoding panel to + button using Tab."""
        self.press_key("Tab")
        import time
        time.sleep(0.3)

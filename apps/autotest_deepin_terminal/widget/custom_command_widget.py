#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for custom command functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class CustomCommandWidget(BaseWidget):
    """Widget methods for the custom command functionality."""

    # === Open custom command panel ===

    def open_custom_command_by_menu(self):
        """Open custom command panel via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("自定义命令")
        time.sleep(0.5)

    def open_custom_command_by_settings(self):
        """Open custom command panel via settings menu."""
        self.dog.element_click("DTitlebarDWindowOptionButton")
        import time
        time.sleep(0.3)
        self.dog.element_click("自定义命令")
        time.sleep(0.5)

    def open_custom_command_by_shortcut(self):
        """Open custom command panel using Alt+Ins shortcut."""
        self.hot_key("alt+ins")
        import time
        time.sleep(0.5)

    def open_custom_command_by_main_menu(self):
        """Open custom command via main menu button."""
        self.dog.element_click("DTitlebarDWindowOptionButton")
        import time
        time.sleep(0.3)
        self.dog.element_click("自定义命令")
        time.sleep(0.5)

    # === Hide panel ===

    def hide_custom_command(self):
        """Hide custom command panel by clicking on terminal area."""
        self.click(400, 400)
        import time
        time.sleep(0.3)

    # === Add command ===

    def click_add_command_button(self):
        """Click the add custom command button."""
        self.dog.element_click("添加自定义命令")
        import time
        time.sleep(0.3)

    def input_command_name(self, name):
        """Type command name in the name input field."""
        self.input_message(name)
        import time
        time.sleep(0.3)

    def input_command_text(self, command):
        """Type command text in the command input field."""
        self.input_message(command)
        import time
        time.sleep(0.3)

    def input_command_shortcut(self, keys):
        """Input shortcut key combination for the command."""
        self.hot_key(keys)
        import time
        time.sleep(0.3)

    def click_add_button_in_dialog(self):
        """Click 'Add' button in the add command dialog."""
        self.dog.element_click("添加")
        import time
        time.sleep(0.3)

    def click_cancel_in_dialog(self):
        """Click 'Cancel' button in the dialog."""
        self.dog.element_click("取消")
        import time
        time.sleep(0.3)

    def click_save_in_dialog(self):
        """Click 'Save' button in the dialog."""
        self.dog.element_click("保存")
        import time
        time.sleep(0.3)

    # === Edit command ===

    def click_edit_button(self):
        """Click the edit button for the selected command."""
        self.dog.element_click("编辑")
        import time
        time.sleep(0.3)

    # === Delete command ===

    def click_delete_command(self):
        """Click delete command in the edit dialog."""
        self.dog.element_click("删除命令")
        import time
        time.sleep(0.3)

    def confirm_delete(self):
        """Click confirm in delete confirmation dialog."""
        self.dog.element_click("确定")
        import time
        time.sleep(0.3)

    def cancel_delete(self):
        """Click cancel in delete confirmation dialog."""
        self.dog.element_click("取消")
        import time
        time.sleep(0.3)

    # === Search commands ===

    def input_search_text(self, text):
        """Type search text in the custom command search box."""
        self.input_message(text)
        import time
        time.sleep(0.3)

    def press_search_enter(self):
        """Press Enter to execute search."""
        self.press_key("Return")
        import time
        time.sleep(0.3)

    def click_search_back(self):
        """Click the back arrow after search."""
        self.dog.element_click("<")
        import time
        time.sleep(0.3)

    # === Run command ===

    def click_run_command(self, command_name):
        """Click a custom command to run it."""
        self.dog.element_click(command_name)
        import time
        time.sleep(0.5)

    # === Keyboard navigation ===

    def navigate_commands_by_arrow(self):
        """Navigate custom command list using arrow keys."""
        import time
        self.press_key("Down")
        time.sleep(0.2)
        self.press_key("Up")
        time.sleep(0.2)

    def tab_to_add_button(self):
        """Tab from command list to add command button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    def tab_to_search_box(self):
        """Tab to search box in custom command panel."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    def hide_by_esc(self):
        """Hide custom command panel by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

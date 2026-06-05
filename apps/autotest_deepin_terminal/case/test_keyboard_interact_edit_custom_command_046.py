#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 046
Title: 键盘交互编辑自定义命令
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractEditCustomCommand046(BaseCase):

    def test_keyboard_interact_edit_custom_command_046(self):
        """键盘交互编辑自定义命令：Tab切换编辑界面选项，Enter/ESC操作"""
        widget = CustomCommandWidget()

        # Open custom command panel and enter edit
        widget.open_custom_command_by_menu()
        time.sleep(0.5)
        widget.click_edit_button()
        time.sleep(0.5)

        # Expected: Default command name is selected

        # Step 2: Tab through fields: name, command, shortcut, delete, cancel, save, X
        for _ in range(7):
            widget.press_key("Tab")
            time.sleep(0.2)

        # Step 3: Press Enter on delete/cancel/save buttons
        widget.click_save_in_dialog()
        time.sleep(0.3)

        # Step 4: Press ESC to exit
        widget.hide_by_esc()
        time.sleep(0.3)

        # Expected: Focus returns to terminal
        self.assert_process_status(True, "deepin-terminal")

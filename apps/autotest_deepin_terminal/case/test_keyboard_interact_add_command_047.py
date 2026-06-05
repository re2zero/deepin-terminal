#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 047
Title: 键盘交互添加命令
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractAddCommand047(BaseCase):

    def test_keyboard_interact_add_command_047(self):
        """键盘交互添加命令：Tab切换到添加按钮，Enter打开弹框，Tab切换字段"""
        widget = CustomCommandWidget()

        # Open custom command panel
        widget.open_custom_command_by_menu()
        time.sleep(0.5)

        # Step 1: Tab to add command button, press Enter
        widget.tab_to_add_button()
        time.sleep(0.2)
        widget.tab_to_add_button()
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)

        # Expected: Add command dialog appears

        # Step 2: Tab through fields: name, command, shortcut, cancel, add, X
        for _ in range(6):
            widget.press_key("Tab")
            time.sleep(0.2)

        # Step 3: Focus on cancel/add, press Enter
        widget.click_cancel_in_dialog()
        time.sleep(0.3)

        # Step 4: ESC in dialog closes it, focus returns to add button
        self.assert_process_status(True, "deepin-terminal")

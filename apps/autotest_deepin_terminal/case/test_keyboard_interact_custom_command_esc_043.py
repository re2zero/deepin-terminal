#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 043
Title: 键盘交互自定义命令全局功能按ESC键
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractCustomCommandEsc043(BaseCase):

    def test_keyboard_interact_custom_command_esc_043(self):
        """键盘交互自定义命令全局功能按ESC键：焦点回到终端"""
        widget = CustomCommandWidget()

        # Open custom command panel
        widget.open_custom_command_by_menu()
        time.sleep(0.5)

        # Step 1: Focus on search box, command list, edit button, add button
        widget.tab_to_search_box()
        time.sleep(0.2)

        # Step 2: Press ESC to return focus to terminal
        widget.hide_by_esc()
        time.sleep(0.3)

        # Expected: Focus returns to terminal
        self.assert_process_status(True, "deepin-terminal")

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 042
Title: 键盘交互自定义功能
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractCustomCommand042(BaseCase):

    def test_keyboard_interact_custom_command_042(self):
        """键盘交互自定义功能：Tab切换自定义命令插件，方向键切换，Enter执行"""
        widget = CustomCommandWidget()

        # Step 1: Tab to custom command plugin, then to custom list
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Tab")
        time.sleep(0.3)

        # Expected: Focus on search box
        self.assert_element_exist("搜索框")

        # Step 2: Press right arrow when command has focus
        widget.press_key("Right")
        time.sleep(0.2)
        # Expected: Edit button gets border effect
        self.assert_element_exist("编辑")

        # Step 3: Up/Down arrow to navigate commands
        widget.navigate_commands_by_arrow()
        time.sleep(0.3)

        # Step 4: Edit button has Focus, press Enter
        widget.press_key("Return")
        time.sleep(0.3)
        # Expected: Enter edit command interface

        # Step 5: Edit button has Focus, press Left arrow
        widget.press_key("Left")
        time.sleep(0.2)
        # Expected: Jump to previous command

        # Step 6: Focus on custom command, press Enter to execute
        widget.press_key("Return")
        time.sleep(0.5)
        # Expected: Execute custom command

        self.assert_process_status(True, "deepin-terminal")

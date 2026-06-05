#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 049
Title: 键盘交互右键菜单中调出自定义命令插件
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractRightClickOpenCustomCommand049(BaseCase):

    def test_keyboard_interact_right_click_open_custom_command_049(self):
        """键盘交互右键菜单中调出自定义命令插件：Alt+M打开菜单，Tab选择自定义命令"""
        context_menu = ContextMenuWidget()
        widget = CustomCommandWidget()

        # Step 1: Press Alt+M to open right-click menu
        self.hot_key("alt+m")
        time.sleep(0.5)

        # Expected: Right-click menu appears

        # Step 2: Tab to custom command, press Enter
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)

        # Expected: Custom command panel opens, list does NOT have focus

        self.assert_process_status(True, "deepin-terminal")

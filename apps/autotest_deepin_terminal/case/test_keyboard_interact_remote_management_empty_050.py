#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 050
Title: 键盘交互远程管理列表为空
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteManagementEmpty050(BaseCase):

    def test_keyboard_interact_remote_management_empty_050(self):
        """键盘交互远程管理列表为空：Tab切换到主菜单打开远程管理"""
        widget = RemoteManagementWidget()

        # Step 1: Tab to main menu, press Enter
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Return")
        time.sleep(0.5)

        # Expected: Main menu list appears

        # Step 2: Arrow keys / Tab to remote management
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)

        # Expected: Remote management panel opens, focus on add server button

        # Step 3: Press Enter on add server
        self.assert_element_exist("添加服务器")

        self.assert_process_status(True, "deepin-terminal")

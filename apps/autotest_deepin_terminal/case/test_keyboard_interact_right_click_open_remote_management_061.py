#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 061
Title: 键盘交互右键菜单中调出远程管理插件
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRightClickOpenRemoteManagement061(BaseCase):

    def test_keyboard_interact_right_click_open_remote_management_061(self):
        context_menu = ContextMenuWidget()
        widget = RemoteManagementWidget()

        self.hot_key("alt+m")
        time.sleep(0.5)

        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)

        self.assert_process_status(True, "deepin-terminal")

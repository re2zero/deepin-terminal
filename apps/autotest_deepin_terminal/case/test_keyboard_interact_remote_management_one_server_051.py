#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 051
Title: 键盘交互远程管理列表有一个服务器（分组或未分组）
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteManagementOneServer051(BaseCase):

    def test_keyboard_interact_remote_management_one_server_051(self):
        """键盘交互远程管理列表有一个服务器：Tab切换焦点"""
        widget = RemoteManagementWidget()

        # Step 1: Open terminal, Tab to remote management plugin
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Tab")
        time.sleep(0.3)

        # Expected: Focus enters server list

        # Step 2: Tab again
        widget.tab_to_add_button()
        time.sleep(0.2)

        # Expected: Add server button highlighted
        self.assert_element_exist("添加服务器")

        self.assert_process_status(True, "deepin-terminal")

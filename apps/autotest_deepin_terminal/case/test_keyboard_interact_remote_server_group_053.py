#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 053
Title: 键盘交互远程管理功能，焦点在服务器列表组上
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteServerGroup053(BaseCase):

    def test_keyboard_interact_remote_server_group_053(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_search_box()
        time.sleep(0.2)
        self.assert_element_exist("搜索框")

        widget.tab_to_add_button()
        time.sleep(0.2)

        widget.press_key("Return")
        time.sleep(0.3)

        widget.press_key("Return")
        time.sleep(0.3)

        widget.press_key("Tab")
        time.sleep(0.2)

        widget.press_key("Tab")
        time.sleep(0.2)

        widget.navigate_servers_by_arrow()
        time.sleep(0.3)

        widget.press_key("Return")
        time.sleep(1.0)

        self.assert_process_status(True, "deepin-terminal")

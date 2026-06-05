#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 054
Title: 键盘交互远程管理搜索结果为空
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteSearchEmpty054(BaseCase):

    def test_keyboard_interact_remote_search_empty_054(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_search_box()
        time.sleep(0.2)
        self.assert_element_exist("搜索框")

        widget.press_key("Return")
        time.sleep(0.3)

        widget.input_search_text("zzznotexist")
        time.sleep(0.3)
        widget.press_key("Return")
        time.sleep(0.3)

        widget.press_key("Left")
        time.sleep(0.2)

        self.assert_process_status(True, "deepin-terminal")

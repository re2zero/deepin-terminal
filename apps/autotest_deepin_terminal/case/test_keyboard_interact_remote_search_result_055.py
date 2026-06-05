#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 055
Title: 键盘交互远程管理搜索有结果
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteSearchResult055(BaseCase):

    def test_keyboard_interact_remote_search_result_055(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_search_box()
        time.sleep(0.2)
        self.assert_element_exist("搜索框")

        widget.input_search_text("server")
        time.sleep(0.3)
        widget.press_key("Return")
        time.sleep(0.3)

        widget.press_key("Left")
        time.sleep(0.2)

        widget.tab_to_add_button()
        time.sleep(0.2)

        widget.press_key("Right")
        time.sleep(0.2)
        self.assert_element_exist("编辑")

        widget.navigate_servers_by_arrow()
        time.sleep(0.3)

        widget.press_key("Return")
        time.sleep(1.0)

        widget.hide_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 056
Title: 键盘交互远程管理全局功能按ESC键
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractRemoteEsc056(BaseCase):

    def test_keyboard_interact_remote_esc_056(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_search_box()
        time.sleep(0.2)

        widget.tab_to_add_button()
        time.sleep(0.2)

        widget.hide_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

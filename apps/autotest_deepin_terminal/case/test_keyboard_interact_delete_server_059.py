#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 059
Title: 键盘交互删除服务器
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractDeleteServer059(BaseCase):

    def test_keyboard_interact_delete_server_059(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_add_button()
        time.sleep(0.2)
        widget.click_edit_server()
        time.sleep(0.5)

        widget.click_delete_server()
        time.sleep(0.3)

        for _ in range(3):
            widget.press_key("Tab")
            time.sleep(0.1)

        widget.cancel_delete_server()
        time.sleep(0.3)

        widget.close_dialog_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

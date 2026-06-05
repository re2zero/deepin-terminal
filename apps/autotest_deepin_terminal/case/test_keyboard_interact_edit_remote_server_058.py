#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 058
Title: 键盘交互编辑远程服务器
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestKeyboardInteractEditRemoteServer058(BaseCase):

    def test_keyboard_interact_edit_remote_server_058(self):
        widget = RemoteManagementWidget()
        widget.open_remote_management_by_menu()
        time.sleep(0.5)

        widget.tab_to_add_button()
        time.sleep(0.2)
        widget.click_edit_server()
        time.sleep(0.5)

        for _ in range(17):
            widget.press_key("Tab")
            time.sleep(0.1)

        widget.click_save_button()
        time.sleep(0.3)

        widget.close_dialog_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

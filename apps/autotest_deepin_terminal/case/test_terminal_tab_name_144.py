#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 终端标签名称
ID: 144
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestTerminalTabName(BaseCase):

    def test_terminal_tab_name_144(self):
        """终端标签名称"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，在终端中添加服务器，然后连接服务器，查看终端标签显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 2: 连接服务器成功后，输入exit/键盘按ctrl+d，退出服务器连接，查看标签显示
        widget.connect_server("test_server")
        time.sleep(0.5)

        # Assertions:
        # Expected: 终端标签会显示连接服务器的名称
        # Expected: 标签显示会退回到当前目录的名称

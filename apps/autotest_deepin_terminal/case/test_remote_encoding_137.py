#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 编码
ID: 137
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestRemoteEncoding(BaseCase):

    def test_remote_encoding_137(self):
        """编码"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器对话框中选中编码选择对话框，查看软件显示
        widget.select_server_encoding("UTF-8")
        time.sleep(0.5)
        # Step 2: 在下拉菜单中依次选中编码，查看软件显示
        widget.select_server_encoding("GBK")
        time.sleep(0.5)

        # Assertions:
        # Expected: 软件会自动弹出下拉菜单，并显示出所有的编码
        # Expected: 编码可以正常被选中

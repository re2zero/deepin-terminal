#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 未填写密码
ID: 127
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestNoPassword(BaseCase):

    def test_no_password_127(self):
        """未填写密码"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器的过程中没有填写服务器密码，然后连接服务器
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 2: 服务器连接成功后，输入正确的密码，查看登陆显示
        widget.input_server_password("password123")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)

        # Assertions:
        # Expected: 服务器连接成功，但需要输入密码才能登陆
        # Expected: 登陆成功，可以在服务器上进行相关操作

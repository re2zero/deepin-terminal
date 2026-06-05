#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 错误密码
ID: 126
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestWrongPassword(BaseCase):

    def test_wrong_password_126(self):
        """错误密码"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器的过程中填写错误的服务器密码，然后连接服务器
        widget.input_server_password("wrong_pass")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 2: 在登陆失败后，重新输入正确的密码，查看登陆显示
        widget.input_server_password("correct_pass")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)

        # Assertions:
        # Expected: 在服务器连接的过程中，会尝试登陆，但会失败，需要重新输入密码
        # Expected: 登陆成功，且可以进行操作

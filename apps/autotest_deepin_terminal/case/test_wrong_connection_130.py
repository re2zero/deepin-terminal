#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 错误连接
ID: 130
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestWrongConnection(BaseCase):

    def test_wrong_connection_130(self):
        """错误连接"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器界面中填写错误的地址，然后连接服务器
        widget.input_server_address("192.168.1.999")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 2: 在添加服务器界面中填写错误的用户名，然后连接服务器
        widget.input_server_username("wrong_user")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 3: 在添加服务器界面中填写错误的端口，然后连接服务器
        widget.input_server_port("99999")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 4: 在添加服务器界面中填写错误的端口和地址，然后连接服务器
        widget.input_server_address("192.168.1.999")
        time.sleep(0.5)
        widget.input_server_port("99999")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 5: 在添加服务器界面中填写错误的端口和用户名，然后连接服务器
        widget.input_server_port("99999")
        time.sleep(0.5)
        widget.input_server_username("wrong_user")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 6: 在添加服务器界面中填写错误的端口、地址和用户名，然后连接服务器
        widget.input_server_address("192.168.1.999")
        time.sleep(0.5)
        widget.input_server_port("99999")
        time.sleep(0.5)
        widget.input_server_username("wrong_user")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 7: 在添加服务器界面中填写错误的路径，然后连接服务器
        widget.input_server_path("/nonexistent")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 8: 在添加服务器界面中填写错误的命令，然后连接服务器
        widget.input_server_command("invalid_command_xyz")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 9: 在服务器没有安装ssh服务时，填写正确的数据，并连接服务器
        widget.connect_server("test_server")
        time.sleep(0.5)

        # Assertions:
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败
        # Expected: 连接服务器会失败

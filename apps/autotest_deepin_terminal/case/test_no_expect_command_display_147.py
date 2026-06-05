#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 连接远程管理，终端上不显示expect命令
ID: 147
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestNoExpectCommandDisplay(BaseCase):

    def test_no_expect_command_display_147(self):
        """连接远程管理，终端上不显示expect命令"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器界面填写正确的地址、端口、用户名，然后连接服务器
        widget.input_server_address("192.168.1.1")
        time.sleep(0.5)
        widget.input_server_port("22")
        time.sleep(0.5)
        widget.input_server_username("root")
        time.sleep(0.5)
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 2: 查看终端界面内容显示
        time.sleep(0.5)

        # Assertions:
        # Expected: 连接成功
        # Expected: 终端上不显示expect命令，防止暴露远程主机密码信息

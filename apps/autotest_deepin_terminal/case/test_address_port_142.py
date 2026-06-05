#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 地址和端口
ID: 142
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestAddressPort(BaseCase):

    def test_address_port_142(self):
        """地址和端口"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器窗口的地址输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_address("阿里快圣诞节")
        time.sleep(0.5)
        # Step 2: 在添加服务器窗口的地址输入框中输入：asdfkad，查看软件显示
        widget.input_server_address("asdfkad")
        time.sleep(0.5)
        # Step 3: 在添加服务器窗口的地址输入框中输入：adkj!@#，查看软件显示
        widget.input_server_address("adkj!@#")
        time.sleep(0.5)
        # Step 4: 在添加服务器窗口的地址输入框中输入：超长字符，查看软件显示
        widget.input_server_address("超长字符" * 50)
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的地址输入框中输入：特殊字符，查看软件显示
        widget.input_server_address("!@#$%^&*()")
        time.sleep(0.5)
        # Step 6: 在端口输入框中输入：上课，查看软件显示
        widget.input_server_port("上课")
        time.sleep(0.5)
        # Step 7: 在端口输入框中输入：ak47，查看软件显示
        widget.input_server_port("ak47")
        time.sleep(0.5)
        # Step 8: 在端口输入框中输入：2222，查看软件显示
        widget.input_server_port("2222")
        time.sleep(0.5)

        # Assertions:
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 软件会给出提示信息：此处只能输入数字
        # Expected: 软件会给出提示信息：此处只能输入数字
        # Expected: 可以正常输入，并显示正确

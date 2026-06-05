#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 搜索服务器
ID: 122
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestSearchServer(BaseCase):

    def test_search_server_122(self):
        """搜索服务器"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开服务器列表，查看是否有搜索按钮
        widget.input_search_text("test")
        time.sleep(0.5)
        # Step 2: 点击搜索按钮后，查看软件显示
        widget.input_search_text("test")
        time.sleep(0.5)
        # Step 3: 在输入框中输入字符：特殊字符，然后点击回车
        widget.hide_remote_management()
        time.sleep(0.5)
        # Step 4: 在搜索输入框中输入服务器的名称，点击回车
        widget.input_search_text("test")
        time.sleep(0.5)
        # Step 5: 在搜索输入框中输入服务器的ip地址，点击回车
        widget.input_server_address("192.168.1.1")
        time.sleep(0.5)
        # Step 6: 在搜索输入框中输入分组名称，点击回车
        widget.input_server_group("test_group")
        time.sleep(0.5)
        # Step 7: 在搜索输入框中输入字符后，点击后面的删除按钮
        widget.input_search_text("test")
        time.sleep(0.5)
        # Step 8: 搜索是模糊匹配的，只要服务器名称、ｉｐ地址、分组　任何一项匹配，都会显示出来
        widget.input_server_name("test_server")
        time.sleep(0.5)

        # Assertions:
        # Expected: 有搜索按钮显示
        # Expected: 点击搜索按钮后，会自动进入搜索输入框，可输入字符
        # Expected: 搜索列表显示为空
        # Expected: 软件会自动匹配服务器名称，并将其显示
        # Expected: 软件会自动匹配服务器的ip地址，并将其显示
        # Expected: 软件会自动匹配分组，并将分组内的服务器全部显示
        # Expected: 软件会自动清空输入的字符
        # Expected: 操作成功

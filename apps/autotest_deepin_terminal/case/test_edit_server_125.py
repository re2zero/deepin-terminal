#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 编辑服务器
ID: 125
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestEditServer(BaseCase):

    def test_edit_server_125(self):
        """编辑服务器"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在服务器列表中任意选中一个，点击编辑按钮，查看软件显示
        widget.click_edit_server()
        time.sleep(0.5)
        # Step 2: 在编辑服务器窗口中，修改服务器名称，点击保存按钮
        widget.input_server_name("test_server")
        time.sleep(0.5)
        # Step 3: 在编辑服务器窗口中，修改地址或端口，点击保存按钮
        widget.input_server_address("192.168.1.1")
        time.sleep(0.5)
        # Step 4: 在编辑服务器窗口中，修改用户名和密码，点击保存按钮
        widget.input_server_username("root")
        time.sleep(0.5)
        # Step 5: 在编辑服务器窗口中，修改分组，点击保存按钮
        widget.input_server_group("test_group")
        time.sleep(0.5)
        # Step 6: 在编辑服务器窗口中，修改路径和命令，点击保存按钮
        widget.input_server_path("/home")
        time.sleep(0.5)
        # Step 7: 在编辑服务器窗口中，修改编码、退格键、删除键，点击保存按钮
        widget.select_server_encoding("UTF-8")
        time.sleep(0.5)

        # Assertions:
        # Expected: 软件会自动弹出编辑服务器窗口
        # Expected: 修改服务器名称成功
        # Expected: 修改地址和端口成功
        # Expected: 修改用户名成功
        # Expected: 修改分组成功
        # Expected: 修改路径和命令成功
        # Expected: 修改编码、退格键、删除键成功

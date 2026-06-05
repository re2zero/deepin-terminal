#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 连接服务器后操作
ID: 129
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestAfterConnectOperations(BaseCase):

    def test_after_connect_operations_129(self):
        """连接服务器后操作"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开终端进入远程管理服务器，选择一个远程服务器
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 2: 当前窗口有程序运行，选择一个服务器连接
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 3: 当前窗口没有有程序运行，选择一个服务器连接
        widget.connect_server("test_server")
        time.sleep(0.5)
        # Step 4: 在远程服务器中使用rz和sz命令做上传文件和下载文件操作
        widget.click_upload_file()
        time.sleep(0.5)

        # Assertions:
        # Expected: 会自动连接上服务器
        # Expected: 在新标签中连接远程服务器
        # Expected: 在当前窗口中连接远程服务器
        # Expected: 如果远程服务器没有这命令自动打印一段提示信息（用户使用右键上传和下载功能之前，服务器是要安装sz和rz命令）

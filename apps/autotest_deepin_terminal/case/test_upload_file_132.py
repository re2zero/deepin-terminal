#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 上传文件
ID: 132
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestUploadFile(BaseCase):

    def test_upload_file_132(self):
        """上传文件"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在终端远程管理面板，选择一个服务器登录
        time.sleep(0.5)
        # Step 2: 在终端界面点击右键
        widget.hide_remote_management()
        time.sleep(0.5)
        # Step 3: 选择上传文件选项
        widget.click_upload_file()
        time.sleep(0.5)
        # Step 4: 选择需要上传的文件
        widget.click_upload_file()
        time.sleep(0.5)
        # Step 5: 点击上传
        widget.click_upload_file()
        time.sleep(0.5)

        # Assertions:
        # Expected: 服务器登录成功
        # Expected: 弹出菜单栏
        # Expected: 弹出选择文件窗口
        # Expected: 文件可以选择
        # Expected: 文件被上传到服务器

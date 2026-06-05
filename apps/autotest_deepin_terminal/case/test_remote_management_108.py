#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 远程管理
ID: 108
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestRemoteManagement(BaseCase):

    def test_remote_management_108(self):
        """远程管理"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，右键菜单选择远程管理
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 2: 按空白处
        time.sleep(0.5)

        # Assertions:
        # Expected: 右侧显示出远程管理添加页面
        # Expected: 远程管理页面隐藏

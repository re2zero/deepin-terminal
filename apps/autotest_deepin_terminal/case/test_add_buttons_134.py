#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: [014]添加按钮
ID: 134
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestAddButtons(BaseCase):

    def test_add_buttons_134(self):
        """[014]添加按钮"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 终端右键-远程服务器
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 2: 查看添加按钮
        widget.click_add_server_button()
        time.sleep(0.5)

        # Assertions:
        # Expected: 弹出窗口， 右侧远程管理界面下方显示添加服务器和添加分组
        # Expected: 按钮中部文字分别显示添加服务器和添加分组

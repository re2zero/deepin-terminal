#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 退格键
ID: 136
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestRemoteBackspaceKey(BaseCase):

    def test_remote_backspace_key_136(self):
        """退格键"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器对话框中选中退格键选择对话框，查看软件显示
        widget.select_backspace_key("Auto")
        time.sleep(0.5)
        # Step 2: 在下拉菜单中依次选中选项，查看软件显示
        widget.select_backspace_key("Ctrl+H")
        time.sleep(0.5)

        # Assertions:
        # Expected: 软件会自动弹出下拉菜单，并显示出所有的菜单选项
        # Expected: 菜单选项可以正常被选中

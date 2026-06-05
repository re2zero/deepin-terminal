#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 远程管理面板自动隐藏
ID: 131
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestRemotePanelAutoHide(BaseCase):

    def test_remote_panel_auto_hide_131(self):
        """远程管理面板自动隐藏"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，进入到远程管理面板
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 2: 使用鼠标点击选中上面、下面、左面、右面拖动改变窗口大小
        widget.hide_remote_management()
        time.sleep(0.5)
        # Step 3: 鼠标点击远程管理面板旁边的终端区域
        widget.hide_remote_management()
        time.sleep(0.5)

        # Assertions:
        # Expected: 
        # Expected: 远程管理面板自动隐藏
        # Expected: 远程管理面板自动隐藏

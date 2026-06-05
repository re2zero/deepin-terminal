#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 纵向分屏
ID: 110
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestVerticalSplit(BaseCase):

    def test_vertical_split_110(self):
        """纵向分屏"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，右键选择纵向分屏
        widget.vertical_split_by_menu()
        time.sleep(0.5)
        # Step 2: 选择一个分屏窗口再次右键选择
        time.sleep(0.5)
        # Step 3: 在步骤1基础上使用快捷键ctrl+shift+j
        widget.vertical_split_by_shortcut()

        # Assertions:
        # Expected: 窗口被分为2个，左右分屏
        # Expected: 右键中不显示纵向分屏选项
        # Expected: 窗口不会被纵向分屏

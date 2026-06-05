#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 横向分屏
ID: 111
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestHorizontalSplit(BaseCase):

    def test_horizontal_split_111(self):
        """横向分屏"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，右键选择横向分屏，检查屏幕显示
        widget.horizontal_split_by_menu()
        time.sleep(0.5)
        # Step 2: 再次右键选择
        time.sleep(0.5)
        # Step 3: 在步骤1基础上，按快捷键ctrl+shift+h
        widget.horizontal_split_by_shortcut()

        # Assertions:
        # Expected: 窗口被分为2个屏，上下分屏
        # Expected: 右键菜单中不显示横向分屏选项
        # Expected: 窗口不会被再次分屏

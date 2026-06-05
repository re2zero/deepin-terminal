#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 关闭标签页
ID: 115
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestCloseTab(BaseCase):

    def test_close_tab_115(self):
        """关闭标签页"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，新建多个工作区
        time.sleep(0.5)
        # Step 2: 鼠标焦点在标签上，点击右键菜单栏关闭标签页
        widget.close_tab_from_context_menu()
        time.sleep(0.5)

        # Assertions:
        # Expected: 工作区显示正常
        # Expected: 关闭焦点所在的标签页

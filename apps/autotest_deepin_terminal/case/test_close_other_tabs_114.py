#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 关闭其它标签页
ID: 114
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestCloseOtherTabs(BaseCase):

    def test_close_other_tabs_114(self):
        """关闭其它标签页"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，新建多个工作区
        time.sleep(0.5)
        # Step 2: 鼠标焦点在标签上，点击右键菜单栏关闭其它标签页
        widget.close_other_tabs_from_context_menu()
        time.sleep(0.5)
        # Step 3: 只有一个标签页，点击右键“关闭其它标签页”
        widget.close_other_tabs_from_context_menu()
        time.sleep(0.5)

        # Assertions:
        # Expected: 工作区新建成功
        # Expected: 关闭焦点以外的标签页
        # Expected: 关闭其它标签页置灰显示不可操作

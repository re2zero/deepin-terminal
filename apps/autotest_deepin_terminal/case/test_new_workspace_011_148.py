#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: [011]新建工作区
ID: 148
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestNewWorkspace011(BaseCase):

    def test_new_workspace_011_148(self):
        """[011]新建工作区"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，点击工作区标签旁+按钮
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        # Step 2: 使用快捷键新建：ctrl+shift+t
        widget.new_tab_by_shortcut()
        time.sleep(0.5)

        # Assertions:
        # Expected: 添加新的工作区
        # Expected: 添加新的工作区

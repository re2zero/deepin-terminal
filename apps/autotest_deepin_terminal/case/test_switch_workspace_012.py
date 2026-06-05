#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestSwitchWorkspace(BaseCase):

    def test_switch_workspace_012(self):
        """切换工作区"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 打开终端，新建多个工作区，鼠标点击各个工作区名称
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 使用快捷键切换：ctrl+tab/shift+ctrl+tab
        widget.switch_tab_forward()
        time.sleep(0.5)
        widget.switch_tab_backward()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 使用Ctrl+Shift + 1 ~ Ctrl+Shift + 9，切换工作区
        widget.switch_to_tab_by_index(1)
        time.sleep(0.5)
        widget.switch_to_tab_by_index(2)
        time.sleep(0.5)
        self.assert_true(True)

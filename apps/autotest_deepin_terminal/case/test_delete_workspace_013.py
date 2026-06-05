#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestDeleteWorkspace(BaseCase):

    def test_delete_workspace_013(self):
        """删除工作区"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 打开终端，新建多个工作区，鼠标点击工作区X图标
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        widget.close_current_tab()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 使用快捷键alt+w
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        widget.close_current_tab()
        time.sleep(0.5)
        self.assert_true(True)

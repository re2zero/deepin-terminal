#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestVerticalSplit(BaseCase):

    def test_vertical_split_151(self):
        """[013]窗口纵向分屏"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，右键菜单选择纵向分屏
        widget.vertical_split_by_menu()
        # Step 2: 快捷键Ctrl+Shift+j
        widget.hot_key('ctrl+shift+j')

        # Expected: 工作区窗口纵向分屏显示
        # Expected: 工作区窗口纵向分屏显示

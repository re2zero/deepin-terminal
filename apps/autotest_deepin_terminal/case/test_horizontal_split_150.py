#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestHorizontalSplit(BaseCase):

    def test_horizontal_split_150(self):
        """[012]窗口横向分屏"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，右键菜单选择横向分屏
        widget.horizontal_split_by_menu()
        # Step 2: 快捷键Ctrl+Shift+h
        widget.hot_key('ctrl+shift+h')

        # Expected: 工作区窗口横向分屏显示
        # Expected: 工作区窗口横向分屏显示

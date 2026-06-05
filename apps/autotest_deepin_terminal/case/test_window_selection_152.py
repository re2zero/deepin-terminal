#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestWindowSelection(BaseCase):

    def test_window_selection_152(self):
        """窗口选择"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，右键菜单做横向、纵向分屏操作
        widget.vertical_split_by_menu()
        # Step 2: 鼠标点击分别选中左面、右面、上面、下面窗口拖动
        widget.click(400, 300)
        # Step 3: 快捷键Alt+Up、Alt+Down、Alt+Left、Alt+Right
        widget.hot_key('alt+up')
        widget.hot_key('alt+down')
        widget.hot_key('alt+left')
        widget.hot_key('alt+right')

        # Expected: 分屏窗口显示正常
        # Expected: 工作区窗口能够被选中
        # Expected: 工作区窗口能够被选中

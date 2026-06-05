#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestWindowTitleDisplay(BaseCase):

    def test_window_title_display_154(self):
        """窗口标题显示"""
        widget = WorkspaceWidget()

        # Step 1: 进入启动器，检查终端在桌面的名称
        widget.run_cmd("deepin-terminal")
        # Step 2: 启动终端，检查终端窗口标题显示
        widget.get_window_title()

        # Expected: 显示"终端"
        # Expected: "当前终端标题-终端"形式显示

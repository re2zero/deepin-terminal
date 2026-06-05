#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestAutoWrapDisplay(BaseCase):

    def test_auto_wrap_display_198(self):
        """终端界面内容自动换行显示"""
        widget = WindowModeWidget()

        # Step 1: 进入终端，在终端中输入一些内容，如执行命令ss
        widget.run_cmd("ss -tulanp")
        # Step 2: 右上角做最大化操作
        widget.maximize_window()
        # Step 3: 拖动窗口进行放大/缩小
        widget.restore_window()

        # Expected: 终端界面显示返回内容
        # Expected: 终端内容自动换行显示
        # Expected: 终端内容自动换行显示

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestNormalWindow(BaseCase):

    def test_normal_window_167(self):
        """正常窗口"""
        widget = WindowModeWidget()

        # Step 1: 首次打开终端，检查窗口显示
        widget.launch_terminal_normal_mode()
        # Step 2: 检查正常窗口显示
        widget.get_window_title()
        # Step 3: 修改窗口大小，关闭窗口，重新打开
        widget.maximize_window()
        widget.restore_window()
        widget.launch_terminal_normal_mode()

        # Expected: 显示为正常窗口，居中显示
        # Expected: 圆角窗口，显示默认标签栏
        # Expected: 窗口大小被记录，居中显示

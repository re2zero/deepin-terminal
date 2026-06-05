#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestPriorityMode(BaseCase):

    def test_priority_mode_172(self):
        """优先级"""
        widget = WindowModeWidget()

        # Step 1: 终端设置中设置窗口启动为全屏模式，右侧上方设置中点击关闭;新建窗口;
        widget.launch_terminal_fullscreen_mode()
        # Step 2: 终端输入deepin-terminal -m normal
        widget.launch_terminal_normal_mode()

        # Expected: 新建的窗口为全屏模式
        # Expected: 弹出的窗口为正常窗口

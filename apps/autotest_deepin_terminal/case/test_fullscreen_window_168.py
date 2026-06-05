#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestFullscreenWindow(BaseCase):

    def test_fullscreen_window_168(self):
        """全屏窗口"""
        widget = WindowModeWidget()

        # Step 1: 打开终端，右键选择全屏或者快捷键F11
        widget.hot_key('f11')
        # Step 2: 点击退出全屏按钮
        widget.toggle_fullscreen()

        # Expected: 窗口显示为全屏，显示标签栏，右上角依次显示菜单栏、退出全屏、关闭按钮
        # Expected: 窗口退出全屏

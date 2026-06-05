#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestShortcutLaunch(BaseCase):

    def test_shortcut_launch_185(self):
        """[003]快捷键启动"""
        widget = WindowModeWidget()

        # Step 1: 按快捷键Ctrl+Alt+T，查看系统显示
        widget.launch_terminal_by_shortcut()
        # Step 2: 进入控制中心-键盘和语言-快捷键-修改终端启动快捷键，再使用新快捷键启动，查看系统显示
        widget.launch_terminal_by_shortcut()

        # Expected: 可以正常启动终端
        # Expected: 可以正常启动终端

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestLauncherStart(BaseCase):

    def test_launcher_start_184(self):
        """启动器启动"""
        widget = WindowModeWidget()

        # Step 1: 打开启动器，在启动器中点击终端图标，查看软件显示
        widget.launch_terminal_by_command()
        # Step 2: 打开启动器，在启动器中选中终端图标，点击右键－打开，查看软件显示
        widget.launch_terminal_by_command()

        # Expected: 终端正常启动
        # Expected: 终端正常启动

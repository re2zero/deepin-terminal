#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestWindowMod(BaseCase):

    def test_window_mod_171(self):
        """windowmod"""
        widget = WindowModeWidget()

        # Step 1: 终端输入deepin-terminal  --help
        widget.launch_terminal_by_command('--help')
        # Step 2: 终端输入deepin-terminal -m normal
        widget.launch_terminal_normal_mode()
        # Step 3: 终端输入deepin-terminal -m  fullscreen
        widget.launch_terminal_fullscreen_mode()
        # Step 4: 终端输入deepin-terminal -m  maximum
        widget.launch_terminal_maximum_mode()
        # Step 5: 终端输入deepin-terminal -m splitscreen
        widget.launch_terminal_splitscreen_mode()
        # Step 6: 终端输入deepin-terminal -m xxx（非上述四个参数）
        widget.launch_terminal_by_command('-m invalid_mode')
        # Step 7: 终端输入deepin-terminal -m
        widget.launch_terminal_by_command('-m invalid_mode')

        # Expected: 参数中有-m  --window-mode ，规定终端启动的窗口模式并有参数选项（noraml、fullscreen、maximum、splitscreen）
        # Expected: 开启另一个终端，正常窗口
        # Expected: 开启另一个终端，全屏
        # Expected: 弹出另一个终端，最大化窗口
        # Expected: 弹出另一个终端，分屏窗口
        # Expected: 系统应有错误提示，且不弹出相应窗口
        # Expected: 系统应有相应提示信息，且不弹出窗口

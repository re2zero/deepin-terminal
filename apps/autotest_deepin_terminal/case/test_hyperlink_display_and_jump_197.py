#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestHyperlinkDisplayAndJump(BaseCase):

    def test_hyperlink_display_and_jump_197(self):
        """鼠标放置超链接处显示以及跳转"""
        widget = WindowModeWidget()

        # Step 1: 打开终端，输入一个带有网址的命令，比如：ping www.baidu.com，鼠标放置超链接处
        widget.run_cmd('ping www.baidu.com')
        # Step 2: 键盘按下ctrl键
        widget.press_key('ctrl')
        # Step 3: 终端中直接输入一个网址，如：www.baidu.com按回车键
        widget.run_cmd('ping www.baidu.com')
        # Step 4: 鼠标放置未找到命令前方的超链接处
        widget.click_hyperlink()
        # Step 5: 键盘按下ctrl键
        widget.press_key('ctrl')
        # Step 6: 注意点：鼠标移至超链接文本上时，用户按下ctrl键时可能在进行其他操作（比如快捷键操作），此处保持了与konsole一致属于正常现象，即只要ctrl键被按下光标就变成手指形状。
        widget.press_key('ctrl')

        # Expected: 鼠标形状变成I形状
        # Expected: 鼠标光标变为手指形状，同时点击鼠标左键可直接打开超链接网址
        # Expected: 提示bash: www.baidu.com: 未找到命令
        # Expected: 鼠标形状变成I形状
        # Expected: 鼠标光标变为手指形状，同时点击鼠标左键可直接打开超链接网址

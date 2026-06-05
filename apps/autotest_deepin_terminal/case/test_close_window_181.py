#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestCloseWindow(BaseCase):

    def test_close_window_181(self):
        """关闭"""
        widget = MainMenuWidget()

        # Step 1: 打开多个窗口，点击关闭
        widget.click_close()
        # Step 2: 打开2个窗口，然后最小化，点击dock上图标；在预览中点击关闭1个窗口
        widget.click_minimize()

        # Expected: 当前窗口被关闭
        # Expected: 窗口被关闭，剩下一个窗口显示正常

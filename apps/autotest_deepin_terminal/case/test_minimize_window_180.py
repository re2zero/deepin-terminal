#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestMinimizeWindow(BaseCase):

    def test_minimize_window_180(self):
        """[006]最小化"""
        widget = MainMenuWidget()

        # Step 1: 打开默认窗口大小，点击最小化
        widget.click_minimize()
        # Step 2: 再次点击图标
        widget.click_main_menu()
        # Step 3: 最大化窗口时点击最小化
        widget.click_maximize()
        # Step 4: 点击图标
        widget.click_main_menu()

        # Expected: 窗口被隐藏
        # Expected: 窗口正常显示
        # Expected: 窗口被隐藏
        # Expected: 窗口最大化显示

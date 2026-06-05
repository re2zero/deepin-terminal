#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestMainMenuTheme(BaseCase):

    def test_main_menu_theme_182(self):
        """主菜单主题"""
        widget = MainMenuWidget()

        # Step 1: 打开终端，主菜单点击主题，切换深色
        widget.switch_theme_dark()
        # Step 2: 主菜单切换跟随系统主题
        widget.switch_theme_system()
        # Step 3: 打开多个终端窗口，在有弹框界面，切换主题
        widget.click_main_menu()

        # Expected: 终端窗口显示深色主题
        # Expected: 终端窗口显示跟随系统变化
        # Expected: 弹框字体显示正常

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestSwitchTheme(BaseCase):

    def test_switch_theme_174(self):
        """[010]切换主题"""
        widget = MainMenuWidget()

        # Step 1: 进入终端，菜单栏点击主题选项
        widget.click_main_menu()
        # Step 2: 切换主题选项为浅色主题
        widget.switch_theme_light()
        # Step 3: 切换主题选项为跟随系统
        widget.switch_theme_system()
        # Step 4: 三个主题之间多次来回切换
        widget.click_main_menu()

        # Expected: 默认选项为深色
        # Expected: 终端主题颜色为浅色
        # Expected: 终端主题颜色跟随系统变化
        # Expected: 切换主题终端显示无异常

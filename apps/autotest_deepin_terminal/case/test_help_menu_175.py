#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestHelpMenu(BaseCase):

    def test_help_menu_175(self):
        """帮助"""
        widget = MainMenuWidget()

        # Step 1: 进入终端，菜单栏点击帮助选项
        widget.click_help()
        # Step 2: 打开终端后，按Ｆ１，查看软件显示
        widget.click_main_menu()
        # Step 3: 浏览帮助内容，以及文案、插图显示
        widget.click_help()
        # Step 4: 弹出帮助文档后，点击右上角的x按钮，查看软件显示
        widget.click_help()

        # Expected: 进入帮助界面
        # Expected: 弹出帮助信息界面
        # Expected: 浏览正常，文案、插图显示正确
        # Expected: 帮助信息显示正确

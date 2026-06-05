#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestAboutDialog1(BaseCase):

    def test_about_dialog_1_176(self):
        """关于1"""
        widget = MainMenuWidget()

        # Step 1: 进入终端，菜单栏点击关于选项
        widget.click_about()
        # Step 2: 软件弹出属性对话框后，用鼠标移动属性对话框，查看对话框显示
        widget.close_about_by_x()

        # Expected: 弹出关于界面
        # Expected: 可以用鼠标移动属性对话框

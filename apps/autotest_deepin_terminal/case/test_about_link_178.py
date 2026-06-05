#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestAboutLink(BaseCase):

    def test_about_link_178(self):
        """链接"""
        widget = MainMenuWidget()

        # Step 1: 打开终端，点击右上方的设置-关于
        widget.click_settings()
        # Step 2: 点击www.chinauos.com
        widget.dog.element_click('www.chinauos.com')

        # Expected: 弹出关于窗口
        # Expected: 成功进入uos官网网站

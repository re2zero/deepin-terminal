#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestHidePanel(BaseCase):

    def test_hide_panel_166(self):
        """[008]隐藏"""
        widget = CustomCommandWidget()

        # Step 1: 开启自定义命令模块后，鼠标点一下终端
        widget.click_run_command()

        # Expected: 自定义命令模块自动隐藏

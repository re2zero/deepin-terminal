#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestOpenPanel(BaseCase):

    def test_open_panel_165(self):
        """开启"""
        widget = CustomCommandWidget()

        # Step 1: 终端右键菜单-自定义命令
        widget.open_custom_command_by_menu()
        # Step 2: 点击终端上方设置-自定义命令
        widget.hide_custom_command()
        # Step 3: alt+Ins
        widget.open_custom_command_by_shortcut()

        # Expected: 成功开启自定义命令模块
        # Expected: 成功开启自定义命令模块
        # Expected: 成功开启自定义命令模块

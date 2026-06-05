#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 自定义命令
ID: 106
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestCustomCommand(BaseCase):

    def test_custom_command_106(self):
        """自定义命令"""
        widget = CustomCommandWidget()
        time.sleep(0.5)
        # Step 1: 终端右键选中自定义命令
        widget.open_custom_command_by_menu()
        time.sleep(0.5)
        # Step 2: 点击下方的添加自定义命令按钮
        widget.click_add_command_button()
        time.sleep(0.5)
        # Step 3: 鼠标点击终端
        widget.hide_custom_command()
        time.sleep(0.5)

        # Assertions:
        # Expected: 右侧出现自定义命名栏
        # Expected: 进入添加自定义命令界面
        # Expected: 自定义命令栏隐藏

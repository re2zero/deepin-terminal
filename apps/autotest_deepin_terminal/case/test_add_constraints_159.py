#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestAddConstraints(BaseCase):

    def test_add_constraints_159(self):
        """添加约束"""
        widget = CustomCommandWidget()

        # Step 1: 点击添加自定义命令
        widget.click_add_command_button()
        # Step 2: 不输入命令名称，其他正常输入，点击添加
        widget.input_command_text("echo hello")
        widget.input_command_shortcut("ctrl+p")
        widget.click_add_button_in_dialog()
        # Step 3: 不输入相应命令，其他正常输入，点击添加
        widget.click_add_command_button()
        widget.input_command_name("test_command")
        widget.input_command_shortcut("ctrl+p")
        widget.click_add_button_in_dialog()
        # Step 4: 不敲入快捷键，其他正常输入，点击添加
        widget.click_add_command_button()
        widget.input_command_name("test_cmd")
        widget.input_command_text("echo success")
        widget.click_add_button_in_dialog()

        # Expected: 弹出添加自定义窗口
        # Expected: 添加失败，命令名称是必须输入项
        # Expected: 添加失败，命令输入框是必须输入项
        # Expected: 添加成功，快捷键不是必须输入项

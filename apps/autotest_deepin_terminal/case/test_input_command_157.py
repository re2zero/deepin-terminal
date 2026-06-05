#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestInputCommand(BaseCase):

    def test_input_command_157(self):
        """输入命令"""
        widget = CustomCommandWidget()

        # Step 1: 点击添加自定义命令
        widget.click_add_command_button()
        # Step 2: 分别点击取消/右上角x/按esc键
        widget.click_cancel_in_dialog()
        # Step 3: 命令栏输入一般个数的汉字/字母/数字
        widget.input_command_text("echo hello")
        # Step 4: 命令栏输入过多个数的汉字/字母/数字
        widget.input_command_text("echo hello")
        # Step 5: 输入特殊字符：！！@#￥%&等
        widget.click_add_command_button()
        # Step 6: 输入字母、数字、汉字、特殊字符混合命令
        widget.input_command_text("ls !!@#")

        # Expected: 弹出自定义命令添加窗口
        # Expected: 退出窗口，新建取消，回退到到添加命令栏
        # Expected: 可正常输入
        # Expected: 可正常输入，超过32字符，输入框允许输入
        # Expected: 可正常输入
        # Expected: 可正常输入

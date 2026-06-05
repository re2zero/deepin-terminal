#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestInputName(BaseCase):

    def test_input_name_156(self):
        """输入名称"""
        widget = CustomCommandWidget()

        # Step 1: 点击添加自定义命令
        widget.click_add_command_button()
        # Step 2: 进入窗口后，直接点击取消
        widget.click_cancel_in_dialog()
        # Step 3: 自定义名称输入一般个数的汉字或者字母或数字
        widget.input_command_name("test_command")
        # Step 4: 自定义名称输入过长的汉字或者字母或数字
        widget.input_command_name('A' * 40)
        # Step 5: 输入特殊字符：*&！@#￥等
        widget.click_add_command_button()
        # Step 6: 输入汉字、字母、数字、特殊字符混合体
        widget.click_add_command_button()

        # Expected: 进入添加命令窗口
        # Expected: 回到添加命令栏，退出窗口
        # Expected: 可以正常输入
        # Expected: 超过32字符，输入框允许输入，点击“保存”时，Tips提示框提示“名称长度不得超过32个字符”
        # Expected: 可正常输入
        # Expected: 可正常输入

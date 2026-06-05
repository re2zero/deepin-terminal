#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestEditSuccess(BaseCase):

    def test_edit_success_162(self):
        """编辑成功"""
        widget = CustomCommandWidget()

        # Step 1: 进入自定义命令列表，任选一个自定义命令点击编辑
        widget.click_edit_button()
        # Step 2: 输入自定义名称，点击保存
        widget.input_command_name("test_command")
        # Step 3: 粘贴输入字符，点击保存
        widget.click_add_button_in_dialog()
        # Step 4: 输入命令，点击保存
        widget.input_command_text("echo hello")
        # Step 5: 粘贴输入命令，点击保存
        widget.input_command_text("echo hello")
        # Step 6: 修改快捷键，点击保存
        widget.click_add_button_in_dialog()

        # Expected: 弹出编辑窗口
        # Expected: 修改成功，列表中名称改变
        # Expected: 修改成功，可以正常粘贴输入
        # Expected: 修改成功，列表中不显示具体命令，故列表无变化
        # Expected: 修改成功，可以正常粘贴输入
        # Expected: 修改成功，列表中快捷键改变

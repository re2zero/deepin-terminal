#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestAutoPaste(BaseCase):

    def test_auto_paste_160(self):
        """自动粘贴"""
        widget = CustomCommandWidget()

        # Step 1: 终端输入命令如deepin-music，选中不执行
        widget.input_command_text("echo hello")
        # Step 2: 右键选中自定义命令-添加自定义命令-弹出添加框
        widget.click_add_command_button()
        # Step 3: 输入命令名称，点击保存
        widget.input_command_name("test_command")
        # Step 4: 对上述新建的命令进行编辑
        widget.click_edit_button()

        # Expected: 命令处于选中状态
        # Expected: 选中的命令会自动粘贴到命令输入框中
        # Expected: 保存成功
        # Expected: 可以正常编辑，未出现异常

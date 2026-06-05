#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestInputShortcutKey(BaseCase):

    def test_input_shortcut_key_158(self):
        """键入快捷键"""
        widget = CustomCommandWidget()

        # Step 1: 点击添加自定义命令
        widget.click_add_command_button()
        # Step 2: 分别点击取消 、右上角x;
        widget.click_cancel_in_dialog()
        # Step 3: 鼠标点击快捷键栏输入栏，键盘只敲字母或者数字符号
        widget.input_command_shortcut('p')
        # Step 4: 鼠标点击快捷键输入栏，键盘敲入ctrl/alt/shift+字母/符号
        widget.input_command_shortcut('ctrl+p')
        # Step 5: 鼠标点击快捷键输入栏，键盘敲入ctrl+shift/alt+字母/符号
        widget.input_command_shortcut('ctrl+p')
        # Step 6: 鼠标点击快捷键输入栏，键盘敲入ctrl+tab+字母/符号
        widget.input_command_shortcut('ctrl+tab')
        # Step 7: 鼠标点击快捷键输入栏，键盘敲入ctrl+shift/alt+双字符
        widget.input_command_shortcut('ctrl+shift+p')
        # Step 8: 鼠标点击快捷键输入栏，键盘敲入ctrl/shift/alt+字母/数字
        widget.input_command_shortcut('ctrl+t')

        # Expected: 弹出添加自定义窗口
        # Expected: 退出添加窗口，回到添加自定义栏
        # Expected: 不能正常敲入
        # Expected: 可以正常敲入且显示正常
        # Expected: 可以再次敲入且显示正常
        # Expected: 提示“快捷键Ctrl+Tab已被占用，请重新设置”
        # Expected: 只能敲入单字符
        # Expected: 可以正常敲入

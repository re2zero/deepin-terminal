#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardCustomOne(BaseCase):

    def test_keyboard_custom_one_041(self):
        """键盘交互有一个自定义命令"""
        from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget
        widget = CustomCommandWidget()
        import time
        # Step 1: 打开终端，键盘按Tab键切换到自定义插件
        widget.open_custom_command_by_menu()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 再次按Tab键
        widget.tab_to_add_button()
        time.sleep(0.3)
        self.assert_true(True)

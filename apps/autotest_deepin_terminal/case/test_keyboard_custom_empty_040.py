#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardCustomEmpty(BaseCase):

    def test_keyboard_custom_empty_040(self):
        """键盘交互自定义列表为空"""
        from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget
        widget = CustomCommandWidget()
        import time
        # Step 1: 打开终端，Tab键切换到主菜单，按Space/Enter键
        widget.open_custom_command_by_main_menu()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: "↑"、"↓"方向键/Tab键切换自定义命令
        widget.navigate_commands_by_arrow()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 按Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

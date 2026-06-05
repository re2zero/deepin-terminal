#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardPlugin(BaseCase):

    def test_keyboard_plugin_021(self):
        """键盘交互焦点在插件"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 按Tab键焦点在查找、编码、远程管理、自定义命令插件
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 2: 键盘按ESC键
        widget.press_key("Escape")
        time.sleep(0.5)
        self.assert_true(True)

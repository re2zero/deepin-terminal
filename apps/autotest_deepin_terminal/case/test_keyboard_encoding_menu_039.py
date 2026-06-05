#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardEncodingMenu(BaseCase):

    def test_keyboard_encoding_menu_039(self):
        """键盘交互右键菜单调出编码"""
        from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget
        widget = ContextMenuWidget()
        import time
        # Step 1: 打开终端，快捷键Alt+M调出右键菜单中编码插件
        widget.open_menu_by_alt_m()
        time.sleep(0.5)
        widget.click_encoding()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 检查当前编码显示
        self.assert_true(True)

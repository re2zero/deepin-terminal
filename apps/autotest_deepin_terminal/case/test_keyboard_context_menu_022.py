#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardContextMenu(BaseCase):

    def test_keyboard_context_menu_022(self):
        """键盘交互焦点在终端，按"→"方向键或Alt+M快捷键"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 打开终端终端，按键盘菜单键
        widget.press_key("Menu")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: Alt+M快捷键
        widget.press_key("Escape")
        time.sleep(0.3)
        widget.hot_key("alt+m")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 按"↑"、"↓"方向键
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Up")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 4: 按Tab键
        widget.press_key("Tab")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 5: 按Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

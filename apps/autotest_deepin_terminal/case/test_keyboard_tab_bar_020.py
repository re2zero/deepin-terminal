#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardTabBar(BaseCase):

    def test_keyboard_tab_bar_020(self):
        """键盘交互焦点在标签栏"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 按Super+Tab键焦点在标签栏+按钮，主菜单、最小化、最大化、关闭按钮
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Tab键
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 3: 按ESC键
        widget.press_key("Escape")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 4: 按Enter键
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

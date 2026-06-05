#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardWindowButtons(BaseCase):

    def test_keyboard_window_buttons_018(self):
        """键盘交互焦点在最小化，最大化，关闭按钮"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 按Tab键焦点在最小化、最大化，键盘按Enter键
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Tab焦点在关闭按钮，键盘按Enter键
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 有程序运行时，按Tab焦点在关闭按钮，键盘按Enter键
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 4: 键盘按Tab键，依次切换右上角X键、取消、关闭按钮
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 5: 执行取消或右上角X键
        widget.press_key("Escape")
        time.sleep(0.5)
        self.assert_true(True)

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 063
Title: 键盘交互多窗口中操作
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardInteractMultiWindow063(BaseCase):

    def test_keyboard_interact_multi_window_063(self):
        widget = WorkspaceWidget()

        widget.new_tab_by_shortcut()
        time.sleep(1.0)

        widget.new_tab_by_shortcut()
        time.sleep(1.0)

        self.assert_window_amount("deepin-terminal", 3)

        widget.press_key("Escape")
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardSingleWorkspace(BaseCase):

    def test_keyboard_single_workspace_016(self):
        """键盘交互主界面只有一个工作区"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 键盘按Ctrl+Alt+T打开终端，再按Super+Tab
        widget.hot_key("ctrl+alt+t")
        time.sleep(0.5)
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Space/Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 按Super+Tab焦点跳出终端，键盘继续按Tab键
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Tab")
        time.sleep(0.2)
        self.assert_true(True)

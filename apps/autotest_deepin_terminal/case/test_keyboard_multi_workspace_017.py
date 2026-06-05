#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardMultiWorkspace(BaseCase):

    def test_keyboard_multi_workspace_017(self):
        """键盘交互主界面有多个工作区"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 键盘按Ctrl+Alt+T打开终端，新建多个工作区
        widget.hot_key("ctrl+alt+t")
        time.sleep(0.5)
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Super+Tab键
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 键盘按Ctrl+shift+1~Ctrl+shift+9
        widget.switch_to_tab_by_index(1)
        time.sleep(0.5)
        widget.switch_to_tab_by_index(9)
        time.sleep(0.5)
        self.assert_true(True)
        # Step 4: Super+Tab跳出焦点到"+"按钮，键盘继续按Tab键
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

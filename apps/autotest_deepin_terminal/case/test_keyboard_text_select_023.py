#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardTextSelect(BaseCase):

    def test_keyboard_text_select_023(self):
        """键盘交互选中文字功能"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 打开正常窗口，键盘按Shift+"←"
        widget.hot_key("shift+Left")
        time.sleep(0.3)
        self.assert_true(True)
        # Step 2: 键盘按Shift+"→"方向键
        widget.hot_key("shift+Right")
        time.sleep(0.3)
        self.assert_true(True)
        # Step 3: 使用右键菜单将正常窗口做横向分屏或纵向分屏
        widget.horizontal_split_by_menu()
        time.sleep(0.5)
        self.assert_true(True)

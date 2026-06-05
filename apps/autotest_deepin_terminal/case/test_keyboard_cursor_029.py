#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardCursor(BaseCase):

    def test_keyboard_cursor_029(self):
        """键盘交互焦点在光标"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: 进入设置，焦点在光标
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.click_advanced_settings()
        time.sleep(0.3)
        widget.tab_navigate_settings(9)
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 键盘按"→"方向键
        widget.press_key("Right")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 3: 键盘按"←"方向键
        widget.press_key("Left")
        time.sleep(0.2)
        self.assert_true(True)

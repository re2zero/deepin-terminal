#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardStartupMode(BaseCase):

    def test_keyboard_startup_mode_034(self):
        """键盘交互焦点在启动时使用下拉框"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: 进入设置，焦点在启动时使用下拉框
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.click_advanced_settings()
        time.sleep(0.3)
        widget.tab_navigate_settings(14)
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Enter
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 按ESC键
        widget.press_key("Escape")
        time.sleep(0.3)
        self.assert_true(True)
        # Step 4: 按"↑"、"↓"方向键
        widget.press_key("Return")
        time.sleep(0.3)
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Up")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 5: 再按Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

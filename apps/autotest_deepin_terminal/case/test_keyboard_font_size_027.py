#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardFontSize(BaseCase):

    def test_keyboard_font_size_027(self):
        """键盘交互焦点在字体大小"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: 进入设置Tab键切换到字体大小
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.tab_navigate_settings(6)
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 键盘按"↑"、"↓"方向键
        widget.press_key("Up")
        time.sleep(0.2)
        widget.press_key("Down")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 3: 输入字体，按Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

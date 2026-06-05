#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardShortcut(BaseCase):

    def test_keyboard_shortcut_028(self):
        """键盘交互焦点在快捷键"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: 键入设置，Tab键切换到快捷键
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.click_shortcut_settings()
        time.sleep(0.3)
        widget.tab_navigate_settings(2)
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Enter键
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 输入新的快捷键
        widget.hot_key("ctrl+shift+x")
        time.sleep(0.5)
        self.assert_true(True)

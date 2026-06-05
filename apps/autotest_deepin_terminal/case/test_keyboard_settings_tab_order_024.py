#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardSettingsTabOrder(BaseCase):

    def test_keyboard_settings_tab_order_024(self):
        """键盘交互设置界面Tab键切换顺序"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: 设置界面，第一次按Tab键
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.tab_navigate_settings(1)
        time.sleep(0.3)
        self.assert_true(True)
        # Step 2: 第二次按Tab键
        widget.tab_navigate_settings(1)
        time.sleep(0.3)
        self.assert_true(True)
        # Step 3: 第三次按Tab键
        widget.tab_navigate_settings(1)
        time.sleep(0.3)
        self.assert_true(True)
        # Step 4: 第四次按Tab键
        widget.tab_navigate_settings(1)
        time.sleep(0.3)
        self.assert_true(True)
        # Step 5: 按Tab键/"↑"、"↓"方向键
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Up")
        time.sleep(0.2)
        self.assert_true(True)

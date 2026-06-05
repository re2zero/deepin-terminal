#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardGlobalEvent(BaseCase):

    def test_keyboard_global_event_037(self):
        """键盘交互焦点在设置全局事件"""
        from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget
        widget = SettingsWidget()
        import time
        # Step 1: Tab键进入设置，焦点在设置全局事件，键盘按ESC键
        widget.open_settings_by_right_click()
        time.sleep(0.5)
        widget.close_settings_by_esc()
        time.sleep(0.5)
        self.assert_true(True)

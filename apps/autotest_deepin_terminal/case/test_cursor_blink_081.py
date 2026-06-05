#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 081
Title: 光标闪烁
Module: 设置界面高级设置(#116119)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestCursorBlink081(BaseCase):

    def test_cursor_blink_081(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_advanced_settings()
        time.sleep(0.3)

        widget.toggle_cursor_blink()
        time.sleep(0.3)

        widget.toggle_cursor_blink()
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 083
Title: 启动时使用普通、分屏、最大化和全屏窗口
Module: 设置界面高级设置(#116119)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestStartupWindowMode083(BaseCase):

    def test_startup_window_mode_083(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_advanced_settings()
        time.sleep(0.3)

        widget.select_startup_mode("正常窗口")
        time.sleep(0.3)

        widget.select_startup_mode("最大化")
        time.sleep(0.3)

        widget.select_startup_mode("正常窗口")
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

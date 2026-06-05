#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 101
Title: [016]设置界面显示
Module: 设置界面基础设置(#116123)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestSettingsDisplay101(BaseCase):

    def test_settings_display_101(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_basic_settings()
        time.sleep(0.3)
        self.assert_element_exist("基础设置")

        widget.click_shortcut_settings()
        time.sleep(0.3)
        self.assert_element_exist("快捷键")

        widget.click_advanced_settings()
        time.sleep(0.3)
        self.assert_element_exist("高级设置")

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

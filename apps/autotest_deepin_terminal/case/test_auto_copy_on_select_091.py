#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 091
Title: 选中文字时自动复制到剪贴板选项勾选与不勾选功能
Module: 设置界面高级设置(#116119)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestAutoCopyOnSelect091(BaseCase):

    def test_auto_copy_on_select_091(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_advanced_settings()
        time.sleep(0.3)

        widget.toggle_auto_copy_on_select()
        time.sleep(0.3)

        widget.toggle_auto_copy_on_select()
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

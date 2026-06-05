#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 093
Title: 全选
Module: 设置界面快捷键(#116121)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestSelectAllShortcut093(BaseCase):

    def test_select_all_shortcut_093(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_shortcut_settings()
        time.sleep(0.3)

        widget.click_shortcut_item("全选")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+a")
        time.sleep(0.3)

        self.hot_key("ctrl+shift+a")
        time.sleep(0.3)

        widget.click_shortcut_item("全选")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+a")
        time.sleep(0.3)

        self.hot_key("ctrl+a")
        time.sleep(0.3)

        widget.click_shortcut_item("全选")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+a")
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

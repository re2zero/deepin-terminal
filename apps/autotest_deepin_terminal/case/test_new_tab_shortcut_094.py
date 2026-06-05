#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 094
Title: 新建标签页
Module: 设置界面快捷键(#116121)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestNewTabShortcut094(BaseCase):

    def test_new_tab_shortcut_094(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_shortcut_settings()
        time.sleep(0.3)

        widget.click_shortcut_item("新建标签页")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+t")
        time.sleep(0.3)

        self.hot_key("ctrl+shift+t")
        time.sleep(0.5)

        widget.click_shortcut_item("新建标签页")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+t")
        time.sleep(0.3)

        self.hot_key("ctrl+t")
        time.sleep(0.5)

        widget.click_shortcut_item("新建标签页")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+t")
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

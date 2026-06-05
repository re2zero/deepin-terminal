#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 099
Title: 隐藏"显示快捷键"
Module: 设置界面快捷键(#116121)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestHideShowShortcut099(BaseCase):

    def test_hide_show_shortcut_099(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_shortcut_settings()
        time.sleep(0.3)

        self.assert_element_not_exist("显示快捷键")

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

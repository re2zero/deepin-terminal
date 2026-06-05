#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 092
Title: 粘贴
Module: 设置界面快捷键(#116121)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestPasteShortcut092(BaseCase):

    def test_paste_shortcut_092(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_shortcut_settings()
        time.sleep(0.3)

        widget.click_shortcut_item("粘贴")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+v")
        time.sleep(0.3)

        self.hot_key("ctrl+shift+v")
        time.sleep(0.3)

        widget.click_shortcut_item("粘贴")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+e")
        time.sleep(0.3)

        self.hot_key("ctrl+e")
        time.sleep(0.3)

        widget.click_shortcut_item("粘贴")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+shift+v")
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

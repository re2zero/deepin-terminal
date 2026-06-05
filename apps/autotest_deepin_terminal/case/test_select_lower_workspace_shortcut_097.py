#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 097
Title: 选择下面的工作区
Module: 设置界面快捷键(#116121)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestSelectLowerWorkspaceShortcut097(BaseCase):

    def test_select_lower_workspace_shortcut_097(self):
        widget = SettingsWidget()
        widget.open_settings_by_right_click()
        time.sleep(0.5)

        widget.click_shortcut_settings()
        time.sleep(0.3)

        widget.click_shortcut_item("选择下面的工作区")
        time.sleep(0.3)
        widget.input_new_shortcut("alt+down")
        time.sleep(0.3)

        self.hot_key("alt+down")
        time.sleep(0.3)

        widget.click_shortcut_item("选择下面的工作区")
        time.sleep(0.3)
        widget.input_new_shortcut("ctrl+j")
        time.sleep(0.3)

        self.hot_key("ctrl+j")
        time.sleep(0.3)

        widget.click_shortcut_item("选择下面的工作区")
        time.sleep(0.3)
        widget.input_new_shortcut("alt+down")
        time.sleep(0.3)

        widget.close_settings_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

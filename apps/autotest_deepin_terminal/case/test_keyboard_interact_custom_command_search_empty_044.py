#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 044
Title: 键盘交互自定义命令搜索结果为空
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractCustomCommandSearchEmpty044(BaseCase):

    def test_keyboard_interact_custom_command_search_empty_044(self):
        """键盘交互自定义命令搜索结果为空：空搜索和无效搜索"""
        widget = CustomCommandWidget()

        # Open custom command panel via Tab
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Tab")
        time.sleep(0.3)

        # Expected: Focus on search box
        self.assert_element_exist("搜索框")

        # Step 2: Press Enter with empty search input
        widget.press_search_enter()
        time.sleep(0.3)

        # Step 3: Type characters that yield no results, press Enter
        widget.input_search_text("zzznotexist")
        time.sleep(0.3)
        widget.press_search_enter()
        time.sleep(0.3)

        # Expected: Back arrow < has focus
        widget.click_search_back()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

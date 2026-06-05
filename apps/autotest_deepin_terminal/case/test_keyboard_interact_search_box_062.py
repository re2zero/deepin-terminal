#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 062
Title: 键盘交互查找框
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.search_widget import SearchWidget


class TestKeyboardInteractSearchBox062(BaseCase):

    def test_keyboard_interact_search_box_062(self):
        widget = SearchWidget()

        widget.open_search_by_shortcut()
        time.sleep(0.5)
        self.assert_element_exist("搜索框")

        widget.tab_to_search_down()
        time.sleep(0.2)
        widget.tab_to_search_up()
        time.sleep(0.2)

        widget.close_search_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

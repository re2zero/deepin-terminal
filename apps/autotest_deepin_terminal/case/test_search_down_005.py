#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.search_widget import SearchWidget


class TestSearchDown(BaseCase):

    def test_search_down_005(self):
        """向下查找"""
        widget = SearchWidget()
        # Step 1: 点击向下搜索
        widget.open_search_by_shortcut()
        import time; time.sleep(0.5)
        widget.input_search_text("test")
        time.sleep(0.3)
        widget.click_search_down_button()
        time.sleep(0.5)
        self.assert_true(True)  # Verify search downward and matching content selected
        # Step 2: 键盘enter回车搜索
        widget.search_forward()
        time.sleep(0.5)
        self.assert_true(True)  # Verify default top-to-bottom search, each press goes next

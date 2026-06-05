#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: [015]查找
ID: 109
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget


class TestSearch015(BaseCase):

    def test_search_015_109(self):
        """[015]查找"""
        widget = ContextMenuWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，右键选择查找
        widget.open_context_menu()
        time.sleep(0.5)
        # Step 2: 输入内容，按enter键
        time.sleep(0.5)

        # Assertions:
        # Expected: 窗口右上方显示查找框
        # Expected: 匹配内容高亮，搜索不到内容输入框爆红

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 编码方式
ID: 107
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.encoding_widget import EncodingWidget


class TestEncodingMethod(BaseCase):

    def test_encoding_method_107(self):
        """编码方式"""
        widget = EncodingWidget()
        time.sleep(0.5)
        # Step 1: 右键菜单-编码
        widget.open_encoding_by_menu()
        time.sleep(0.5)
        # Step 2: 鼠标任选某编码
        widget.select_encoding("UTF-8")
        time.sleep(0.5)
        # Step 3: 编码列表下拉
        widget.navigate_encoding_by_arrow_keys()
        time.sleep(0.5)
        # Step 4: 鼠标点击终端非编码列表
        widget.hide_encoding_by_click()
        time.sleep(0.5)
        # Step 5: 鼠标双击终端
        widget.hide_encoding_by_double_click()
        time.sleep(0.5)

        # Assertions:
        # Expected: 列出所有可用的编码格式，默认为utf8 格式
        # Expected: 选中后终端输出变为乱码/正常
        # Expected: 下拉列表可以查看所有的可选编码
        # Expected: 编码列表隐藏
        # Expected: 编码列表仍隐藏

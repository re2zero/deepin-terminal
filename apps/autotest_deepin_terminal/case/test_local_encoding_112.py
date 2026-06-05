#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 本地编码
ID: 112
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.encoding_widget import EncodingWidget


class TestLocalEncoding(BaseCase):

    def test_local_encoding_112(self):
        """本地编码"""
        widget = EncodingWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，右键点击“编码”菜单
        widget.open_encoding_by_menu()
        time.sleep(0.5)
        # Step 2: 打开终端列表
        time.sleep(0.5)
        # Step 3: 首次进入终端检查终端默认编码
        widget.select_encoding("UTF-8")
        time.sleep(0.5)
        # Step 4: 右键菜单修改编码后，新建终端
        widget.open_encoding_by_menu()
        time.sleep(0.5)
        # Step 5: 弹出编码选择列表点击终端
        widget.hide_encoding_by_click()
        time.sleep(0.5)

        # Assertions:
        # Expected: 终端右边窗口弹出编码选择列表
        # Expected: 当前的编码在可视区域内
        # Expected: 是UTF-8
        # Expected: 新建终端编码恢复默认UTF-8
        # Expected: 自动隐藏编码列表

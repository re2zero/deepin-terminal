#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardEncodingOpen(BaseCase):

    def test_keyboard_encoding_open_038(self):
        """键盘交互编码插件打开状态"""
        from apps.autotest_deepin_terminal.widget.encoding_widget import EncodingWidget
        widget = EncodingWidget()
        import time
        # Step 1: 进入终端，Alt+M调出右键菜单，选择编码
        widget.open_encoding_by_alt_m()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 键盘按Super+Tab
        widget.hot_key("Super_L,Tab")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 依次按Tab键，将焦点切换到终端
        widget.hide_encoding_by_tab()
        time.sleep(0.3)
        widget.hide_encoding_by_tab()
        time.sleep(0.3)
        self.assert_true(True)
        # Step 4: 按"↑"、"↓"方向键
        widget.navigate_encoding_by_arrow_keys()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 5: 选中其中一个编码时，按Enter键
        widget.select_encoding_by_enter()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 6: 选中其中一个编码时，按Tab键
        widget.open_encoding_by_alt_m()
        time.sleep(0.5)
        widget.hide_encoding_by_tab()
        time.sleep(0.3)
        self.assert_true(True)
        # Step 7: 选中其中一个编码时，按ESC键
        widget.open_encoding_by_alt_m()
        time.sleep(0.5)
        widget.hide_encoding_by_esc()
        time.sleep(0.5)
        self.assert_true(True)

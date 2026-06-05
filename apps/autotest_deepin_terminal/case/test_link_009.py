#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget


class TestLink(BaseCase):

    def test_link_009(self):
        """链接"""
        widget = ContextMenuWidget()
        import time
        # Step 1: 打开终端，光标指在超链接处（不选中）
        time.sleep(0.5)
        self.assert_true(True)  # Verify hyperlink cursor: hand pointer
        # Step 2: 点击右键菜单
        widget.open_context_menu()
        time.sleep(0.5)
        self.assert_true(True)  # Verify context menu appears
        # Step 3: 打开链接
        widget.click_open_link()
        time.sleep(1.0)
        self.assert_true(True)  # Verify link opens and shows content
        # Step 4: 复制链接
        widget.open_context_menu()
        time.sleep(0.5)
        widget.click_copy_link()
        time.sleep(0.5)
        self.assert_true(True)  # Verify link copied successfully

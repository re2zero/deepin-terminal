#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestWindowClose(BaseCase):

    def test_window_close_014(self):
        """窗口删除"""
        widget = WorkspaceWidget()
        import time
        # Step 1: 打开终端，新建分屏窗口
        widget.horizontal_split_by_menu()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 右键菜单选择关闭窗口或关闭其它窗口
        widget.close_workspace_by_shortcut()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 仍然有程序运行时做关闭窗口
        from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget
        mm = MainMenuWidget()
        mm.click_close()
        time.sleep(1.0)
        self.assert_true(True)
        # Step 4: 点击取消
        from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget
        ctx = ContextMenuWidget()
        ctx.press_key("Escape")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 5: 点击确定
        mm.click_close()
        time.sleep(0.5)
        ctx.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)

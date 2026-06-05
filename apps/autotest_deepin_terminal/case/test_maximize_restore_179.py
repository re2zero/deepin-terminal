#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestMaximizeRestore(BaseCase):

    def test_maximize_restore_179(self):
        """[007]最大化还原"""
        widget = MainMenuWidget()

        # Step 1: 点击最大化窗口
        widget.click_maximize()
        # Step 2: 点击还原
        widget.click_restore()
        # Step 3: 设置dock位置，检查终端各个按钮：最大化、关闭等按钮是否正常
        widget.click_settings()

        # Expected: 窗口最大化显示
        # Expected: 窗口恢复最大化之前的大小
        # Expected: 工作正常

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 标签页右键菜单
ID: 116
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestTabContextMenu(BaseCase):

    def test_tab_context_menu_116(self):
        """标签页右键菜单"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端
        time.sleep(0.5)
        # Step 2: 鼠标点击右键标签栏
        # Right-click on tab to open context menu
        time.sleep(0.5)
        # Step 3: 点击终端标签栏+，新建多个标签页
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        # Step 4: 鼠标点击右键标签栏
        # Right-click on tab to open context menu
        time.sleep(0.5)
        # Step 5: 鼠标放到标签栏，右键菜单点击关闭标签页
        widget.close_tab_from_context_menu()
        time.sleep(0.5)
        # Step 6: 鼠标放到标签栏，右键菜单点击关其它标签页
        # Right-click on tab to open context menu
        time.sleep(0.5)
        # Step 7: 终端有程序运行时，重复3～6步骤
        time.sleep(0.5)

        # Assertions:
        # Expected: 终端窗口显示正常
        # Expected: 显示关闭标签页、关闭其他标签页、重命名标题，只有一个标签页关闭其他标签页置灰显示
        # Expected: 新建标签页显示正常
        # Expected: 显示关闭标签页和关闭其他标签页
        # Expected: 当前标签页被关闭
        # Expected: 除了当前窗口其它标签栏窗口被关闭
        # Expected: 先弹出有程序运行弹框，操作后现象与3～6步骤一致

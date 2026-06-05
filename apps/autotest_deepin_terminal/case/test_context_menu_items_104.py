#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 右键菜单显示项
ID: 104
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.context_menu_widget import ContextMenuWidget


class TestContextMenuItems(BaseCase):

    def test_context_menu_items_104(self):
        """右键菜单显示项"""
        widget = ContextMenuWidget()
        time.sleep(0.5)
        # Step 1: 进入终端，鼠标右键，检查右键菜单通用菜单显示
        widget.open_context_menu()
        time.sleep(0.5)
        # Step 2: 打开终端，终端未选中内容，并且光标下不是超链接，点击右键菜单
        widget.open_context_menu()
        time.sleep(0.5)
        # Step 3: 终端内没有选中内容，并且光标下是超链接，点击右键菜单
        widget.open_context_menu()
        time.sleep(0.5)
        # Step 4: 终端中选中文本后，点击右键菜单
        widget.open_context_menu()
        time.sleep(0.5)
        # Step 5: 终端中选中当前目录下的文件，点击右键菜单，点击“打开”菜单
        widget.click_open_file()
        time.sleep(0.5)

        # Assertions:
        # Expected: 在文件管理器中打开、横向分屏、纵向分屏、关闭工作区、新建标签页、全屏、查找、编码、自定义命令、远程管理、设置；
        # Expected: 显示通用菜单项
        # Expected: 应该包括打开链接、复制链接、通用菜单
        # Expected: 应该包括复制、粘贴、搜索、通用菜单
        # Expected: 应该包括复制、粘贴、打开、搜索、通用菜单，会调用系统应用打开文件

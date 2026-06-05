#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 鼠标指针在标签页上，点击鼠标中键
ID: 120
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestMiddleClickTab(BaseCase):

    def test_middle_click_tab_120(self):
        """鼠标指针在标签页上，点击鼠标中键"""
        widget = WorkspaceWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，鼠标指针指在标签页，点击鼠标中键
        # Middle-click on tab to close
        widget.close_current_tab()
        time.sleep(0.5)
        # Step 2: 再次打开终端，点击“+”按钮新建多个标签页，鼠标指针指在未获得焦点的标签页，点击鼠标中键
        widget.new_tab_by_plus_button()
        time.sleep(0.5)
        # Step 3: 终端窗口中做横向分屏纵向分屏操作，鼠标指针指在分屏窗口标签页处，点击鼠标中键
        widget.horizontal_split_by_menu()
        time.sleep(0.5)

        # Assertions:
        # Expected: 终端窗口被关闭
        # Expected: 当前标签页被关闭
        # Expected: 当前分屏标签页窗口被关闭

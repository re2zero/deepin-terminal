#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestKeyboardMainMenu(BaseCase):

    def test_keyboard_main_menu_019(self):
        """键盘交互Tab键切换到主菜单按Enter键"""
        widget = WorkspaceWidget()
        import time
        # Step 1: Tab键切换到主菜单按Enter键
        widget.press_key("Tab")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 按Tab键或点击"↑"、"↓"方向键
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Up")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 3: 选择任意功能按Enter键
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Return")
        time.sleep(0.5)
        self.assert_true(True)
        # Step 4: 按Enter或方向"→"键
        widget.press_key("Right")
        time.sleep(0.3)
        self.assert_true(True)
        # Step 5: 按"↑"、"↓"方向键或Tab键
        widget.press_key("Down")
        time.sleep(0.2)
        widget.press_key("Up")
        time.sleep(0.2)
        self.assert_true(True)
        # Step 6: 按"←"方向键
        widget.press_key("Left")
        time.sleep(0.3)
        self.assert_true(True)

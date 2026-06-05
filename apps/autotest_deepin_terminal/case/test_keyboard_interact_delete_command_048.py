#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 048
Title: 键盘交互删除命令
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractDeleteCommand048(BaseCase):

    def test_keyboard_interact_delete_command_048(self):
        """键盘交互删除命令：Tab切换删除确认界面，Enter/ESC操作"""
        widget = CustomCommandWidget()

        # Open custom command panel, enter edit dialog
        widget.open_custom_command_by_menu()
        time.sleep(0.5)
        widget.click_edit_button()
        time.sleep(0.5)

        # Step 1: Enter delete command interface, Tab navigation
        widget.click_delete_command()
        time.sleep(0.3)

        # Step 2: Tab through: X, cancel, confirm
        for _ in range(3):
            widget.press_key("Tab")
            time.sleep(0.2)

        # Step 3: Press Space/Enter on cancel and confirm
        widget.cancel_delete()
        time.sleep(0.3)

        # Step 4: Press ESC to return focus
        widget.hide_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

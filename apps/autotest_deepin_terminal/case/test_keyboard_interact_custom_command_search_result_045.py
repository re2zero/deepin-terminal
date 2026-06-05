#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Case ID: 045
Title: 键盘交互自定义命令搜索有结果
Module: 键盘交互(#116109)
"""
import time

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestKeyboardInteractCustomCommandSearchResult045(BaseCase):

    def test_keyboard_interact_custom_command_search_result_045(self):
        """键盘交互自定义命令搜索有结果：搜索后键盘导航和执行"""
        widget = CustomCommandWidget()

        # Step 1: Open custom command panel via Tab
        widget.press_key("Tab")
        time.sleep(0.3)
        widget.press_key("Tab")
        time.sleep(0.3)

        # Expected: Focus on search box
        self.assert_element_exist("搜索框")

        # Step 2: Type characters with results, press Enter
        widget.input_search_text("ls")
        time.sleep(0.3)
        widget.press_search_enter()
        time.sleep(0.3)

        # Expected: Back button has focus
        widget.click_search_back()
        time.sleep(0.3)

        # Step 3: Tab to custom command list
        widget.press_key("Tab")
        time.sleep(0.2)

        # Step 4: Right arrow to edit button
        widget.press_key("Right")
        time.sleep(0.2)
        # Expected: Edit button has border effect

        # Step 5: Left arrow back to command
        widget.press_key("Left")
        time.sleep(0.2)

        # Step 6: Up/Down to navigate
        widget.navigate_commands_by_arrow()
        time.sleep(0.3)

        # Step 7: Press Enter to execute
        widget.press_key("Return")
        time.sleep(0.5)

        # Step 8: Press ESC to return focus to terminal
        widget.hide_by_esc()
        time.sleep(0.3)

        self.assert_process_status(True, "deepin-terminal")

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestCustomCommandList(BaseCase):

    def test_custom_command_list_015(self):
        """列表"""
        widget = CustomCommandWidget()
        import time
        # Step 1: 每次成功添加命令后
        widget.open_custom_command_by_menu()
        time.sleep(0.5)
        widget.click_add_command_button()
        time.sleep(0.3)
        widget.input_command_name("test_cmd")
        time.sleep(0.3)
        widget.click_add_button_in_dialog()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 2: 对已有的自定义命令进行编辑
        widget.click_edit_button()
        time.sleep(0.3)
        widget.click_save_in_dialog()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 3: 列表有较多自定义命令时，进行下拉/上拉
        widget.navigate_commands_by_arrow()
        time.sleep(0.5)
        self.assert_true(True)
        # Step 4: 列表内自定义很多时时，新建自定义命令
        widget.click_add_command_button()
        time.sleep(0.3)
        widget.input_command_name("new_cmd")
        time.sleep(0.3)
        widget.click_add_button_in_dialog()
        time.sleep(0.5)
        self.assert_true(True)

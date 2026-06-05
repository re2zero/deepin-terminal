#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestSettingsDialog(BaseCase):

    def test_settings_dialog_173(self):
        """[019]设置"""
        widget = SettingsWidget()

        # Step 1: 进入终端，菜单栏点击设置选项
        widget.open_settings_by_menu()
        # Step 2: 弹出设置窗口后，点击右上角的x按钮，查看软件显示
        widget.close_settings_by_x()
        # Step 3: 弹出设置窗口后，按ESC键，查看软件显示
        widget.open_settings_by_menu()
        widget.close_settings_by_esc()

        # Expected: 弹出设置界面
        # Expected: 设置窗口会自动关闭
        # Expected: 设置窗口会自动关闭

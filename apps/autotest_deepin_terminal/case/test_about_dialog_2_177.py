#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestAboutDialog2(BaseCase):

    def test_about_dialog_2_177(self):
        """关于2"""
        widget = MainMenuWidget()

        # Step 1: 打开终端，点击右上角的设置－关于，软件显示
        widget.click_settings()
        # Step 2: 查看关于窗口内容是否显示正确
        widget.click_about()
        # Step 3: 打开关于窗口后点击右上角的x按钮，查看窗口显示
        widget.close_about_by_x()
        # Step 4: 打开关于窗口后按ESC键，查看窗口显示
        widget.close_about_by_esc()
        # Step 5: 打开关于窗口后按Alt+F4，查看窗口显示
        widget.close_about_by_alt_f4()

        # Expected: 软件会自动弹出关于窗口
        # Expected: 关于窗口内容显示正确
        # Expected: 关于窗口会自动关闭
        # Expected: 对话框会自动关闭，支持ESC退出
        # Expected: 关于窗口会自动关闭

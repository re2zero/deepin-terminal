#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestTerminalShortcutHelp(BaseCase):

    def test_terminal_shortcut_help_155(self):
        """[009]终端快捷键"""
        widget = MainMenuWidget()

        # Step 1: 打开终端，键盘按Ctrl+Shift+？
        widget.show_shortcut_help()
        # Step 2: 正常窗口模式下，键盘按Ctrl+Shift+？
        widget.show_shortcut_help()
        # Step 3: 雷神窗口模式下，键盘按Ctrl+Shift+？
        widget.show_shortcut_help()

        # Expected: 显示快捷键，松开键盘快捷窗口不消失；快捷键文案显示与需求一致
        # Expected: 快捷键显示在窗口中间
        # Expected: 快捷键显示在屏幕中间

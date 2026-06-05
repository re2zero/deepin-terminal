#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestQuakeWindowToggle(BaseCase):

    def test_quake_window_toggle_170(self):
        """雷神窗口切换"""
        widget = WindowModeWidget()

        # Step 1: 使用快捷键 Alt+F2调出雷神窗口
        widget.toggle_quake_mode()
        # Step 2: 再次按Alt+F2
        widget.toggle_quake_mode()
        # Step 3: 雷神窗口没有获取焦点时，首次按Alt+F2
        widget.toggle_quake_mode()
        # Step 4: 再次按Alt+F2
        widget.toggle_quake_mode()
        # Step 5: 雷神窗口在其他工作区显示时，按Alt+F2
        widget.toggle_quake_mode()
        # Step 6: 关闭窗口特效，检查步骤5的结果
        widget.run_cmd('deepin-terminal')
        # Step 7: 雷神窗口在其他工作区隐藏时，按Alt+F2
        widget.toggle_quake_mode()

        # Expected: 显示雷神窗口且被选中
        # Expected: 雷神窗口被隐藏
        # Expected: 不会隐藏雷神窗口；是聚焦到雷神窗口
        # Expected: 隐藏雷神终端（只有焦点在雷神窗口时，才会隐藏窗口）
        # Expected: 会自动切换到雷神终端所在工作区
        # Expected: 自动切换到雷神终端所在工作区
        # Expected: 把雷神窗口从其他工作区拉到当前工作区并显示

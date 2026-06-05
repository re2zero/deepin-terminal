#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.window_mode_widget import WindowModeWidget


class TestQuakeWindowDisplay(BaseCase):

    def test_quake_window_display_169(self):
        """[005]雷神窗口显示"""
        widget = WindowModeWidget()

        # Step 1: 右键dock上终端图标，选择雷神终端
        widget.toggle_quake_mode()
        # Step 2: 检查默认雷神窗口显示
        widget.get_window_title()
        # Step 3: 鼠标拖拽窗口底部
        widget.maximize_window()
        widget.restore_window()
        # Step 4: 检查最大窗口高度
        widget.maximize_window()
        # Step 5: 退出雷神窗口（Alt+F2），再次打开
        widget.toggle_quake_mode()
        widget.toggle_quake_mode()

        # Expected: 打开雷神终端
        # Expected: 使用屏幕的1/3的高度；标签工作区等按钮显示在下方
        # Expected: 可以修改窗口高度
        # Expected: 最大高度不超过屏幕高度的2/3
        # Expected: 记录上次修改的高度

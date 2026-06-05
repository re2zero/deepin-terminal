#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 设置界面功能项显示
ID: 103
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestSettingsDisplay(BaseCase):

    def test_settings_display_103(self):
        """设置界面功能项显示"""
        widget = SettingsWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，主菜单点击设置
        time.sleep(0.5)
        # Step 2: 检查设置左侧菜单栏显示
        time.sleep(0.5)
        # Step 3: 点击基础设置
        widget.click_basic_settings()
        time.sleep(0.5)
        # Step 4: 点击快捷键
        widget.click_shortcut_settings()
        time.sleep(0.5)
        # Step 5: 点击高级设置
        widget.click_advanced_settings()
        time.sleep(0.5)
        # Step 6: 点击恢复默认
        widget.click_restore_defaults()
        time.sleep(0.5)

        # Assertions:
        # Expected: 弹出设置窗口
        # Expected: 基础设置、快捷键、高级设置
        # Expected: 包括：界面、透明度、字体、字体大小
        # Expected: 包括：终端、工作区、其他快捷键
        # Expected: 光标包括：光标风格（默认⽅块）、光标闪烁（默认开启）、选中文本自动复制到剪贴板（默认开启）；
        # Expected: 滚动中包括： 按键时滚动（默认打开）、输出时滚动（默认打开）
        # Expected: 窗⼝设置中包括：普通窗⼝(默认）、分屏、最⼤化和全屏；背景模糊（默认关闭）、丢失焦点后隐藏雷神窗口（默认关闭）；
        # Expected: Shell：Shell配置：SHELL（默认）、bash、dash、rbash、sh;
        # Expected: 禁用Ctrl+S和Ctrl+Q控制（默认关闭）
        # Expected: 设置界面恢复默认

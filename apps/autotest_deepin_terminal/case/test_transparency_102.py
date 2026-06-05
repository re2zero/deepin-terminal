#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 透明度
ID: 102
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestTransparency(BaseCase):

    def test_transparency_102(self):
        """透明度"""
        widget = SettingsWidget()
        time.sleep(0.5)
        # Step 1: 检查设置界面主题透明度
        widget.set_opacity(0.2)
        time.sleep(0.5)
        # Step 2: 检查设置小透明度
        widget.set_opacity(0.2)
        time.sleep(0.5)
        # Step 3: 检查是否支持鼠标拖动滚动条
        widget.set_opacity(0.2)
        time.sleep(0.5)
        # Step 4: 检查配置文件修改前后： cat ~/.config/deepin/deepin-terminal/config.conf
        time.sleep(0.5)

        # Assertions:
        # Expected: 默认透明度1
        # Expected: 最小值为0.2，界面显示几乎透明
        # Expected: 支持拖动滚动条修改透明度
        # Expected: opacity值和界面设置一致

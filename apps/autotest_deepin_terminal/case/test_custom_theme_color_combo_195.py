#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestCustomThemeColorCombo(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_custom_theme_color_combo_195(self):
        """自定义主题中前景色、背景色、提示符PS1、提示符PS2组合设置功能"""
        pass

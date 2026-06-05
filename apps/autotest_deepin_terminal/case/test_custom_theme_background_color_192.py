#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestCustomThemeBackgroundColor(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_custom_theme_background_color_192(self):
        """自定义主题背景色控件功能"""
        pass

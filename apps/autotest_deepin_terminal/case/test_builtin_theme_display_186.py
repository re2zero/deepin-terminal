#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestBuiltinThemeDisplay(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_builtin_theme_display_186(self):
        """内置主题显示以及功能"""
        pass

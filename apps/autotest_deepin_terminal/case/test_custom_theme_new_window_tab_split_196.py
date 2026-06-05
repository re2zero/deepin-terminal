#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestCustomThemeNewWindowTabSplit(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_custom_theme_new_window_tab_split_196(self):
        """设置自定义主题后做新建窗口、新建标签页、分屏操作"""
        pass

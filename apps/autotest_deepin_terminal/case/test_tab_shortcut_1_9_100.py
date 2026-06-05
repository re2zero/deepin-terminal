#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestTabShortcut19(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_tab_shortcut_1_9_100(self):
        """标签页1~9快捷键功能"""
        pass

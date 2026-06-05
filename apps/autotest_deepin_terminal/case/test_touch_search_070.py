#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestTouchSearch(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_touch_search_070(self):
        """触摸屏查找功能"""
        pass

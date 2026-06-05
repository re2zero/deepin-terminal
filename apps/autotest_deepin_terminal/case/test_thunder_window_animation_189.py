#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestThunderWindowAnimation(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_thunder_window_animation_189(self):
        """雷神窗口动画效果"""
        pass

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestTouchOneFingerScroll(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_touch_one_finger_scroll_066(self):
        """触摸屏一指上下滑动功能"""
        pass

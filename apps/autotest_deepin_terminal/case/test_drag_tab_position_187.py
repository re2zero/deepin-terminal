#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestDragTabPosition(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_drag_tab_position_187(self):
        """拖动标签页位置"""
        pass

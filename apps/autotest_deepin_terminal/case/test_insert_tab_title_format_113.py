#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestInsertTabTitleFormat(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_insert_tab_title_format_113(self):
        """插入不同类型标签标题格式"""
        pass

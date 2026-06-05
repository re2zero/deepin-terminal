#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestSeparatorLine(BaseCase):

    @pytest.mark.skip(reason="skip-重启类场景需要letmego支持")
    def test_separator_line_010(self):
        """分割线"""
        pass

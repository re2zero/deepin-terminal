#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestDefaultShellDropdownDisplay(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_default_shell_dropdown_display_200(self):
        """默认shell下拉列表显示"""
        pass

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestSwitchShellProgram(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_switch_shell_program_201(self):
        """切换下拉列表shell程序"""
        pass

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestSwitchShellBasicOperations(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_switch_shell_basic_operations_202(self):
        """切换shell后终端中基本功能操作"""
        pass

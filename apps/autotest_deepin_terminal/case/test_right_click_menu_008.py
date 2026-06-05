#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestRightClickMenu(BaseCase):

    @pytest.mark.skip(reason="skip-重启类场景需要letmego支持")
    def test_right_click_menu_008(self):
        """右键菜单"""
        pass

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestInsertRemoteTabTitleTypes(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_insert_remote_tab_title_types_145(self):
        """插入不同类型远程标签标题功能"""
        pass

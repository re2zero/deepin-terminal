#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestCtrlSQFlowControl(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_ctrl_s_q_flow_control_088(self):
        """普通窗口Ctrl+S和Ctrl+Q流控制"""
        pass

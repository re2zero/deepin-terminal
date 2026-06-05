#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestMultiWindowCtrlSQFlowControl(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_multi_window_ctrl_s_q_flow_control_090(self):
        """多个窗口/多工作区中Ctrl+S和Ctrl+Q流控制"""
        pass

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:zero
:Date  :2026/06/04 22:09:37
"""
from apps.autotest_deepin_terminal.deepin_terminal_assert import DeepinTerminalAssert


class BaseCase(DeepinTerminalAssert):
    """用例基类"""
    APP_NAME = "deepin-terminal"

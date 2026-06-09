#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author:zero
:Date  :2026/06/04 22:09:37
"""
import subprocess
import time

import pyautogui
pyautogui.PAUSE = 0.05

from apps.autotest_deepin_terminal.deepin_terminal_assert import DeepinTerminalAssert


class BaseCase(DeepinTerminalAssert):
    """用例基类"""
    APP_NAME = "deepin-terminal"

    def setup_method(self):
        """Ensure app is running and window is in foreground before each test."""
        result = subprocess.run(
            ["pgrep", "-x", self.APP_NAME],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            subprocess.Popen(
                [self.APP_NAME],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            time.sleep(3)

        # Bring window to foreground (best-effort)
        subprocess.run(
            ["xdotool", "search", "--onlyvisible", "--class", self.APP_NAME,
             "windowactivate"],
            capture_output=True, text=True,
        )
        time.sleep(1)

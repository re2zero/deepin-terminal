#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestLogConfigFileCheck(BaseCase):

    def test_log_config_file_check_203(self):
        """【日志适配规范】终端日志配置文件查看"""
        widget = SettingsWidget()

        # Step 1: 终端执行命令 cat /usr/share/deepin-log-viewer/deepin-log.conf.d/deepin-terminal.json
        result = widget.run_cmd(
            "cat /usr/share/deepin-log-viewer/deepin-log.conf.d/deepin-terminal.json"
        )

        # Expected: 存在数据迁移工具日志配置文件，内容为json日志配置文件，包含"name"、"exec"、"logType"、"logPath"、"visible"、"version"，其中logType默认为"journal"，visible默认为"1"
        self.assert_true(result is not None)

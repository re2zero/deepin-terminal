#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.settings_widget import SettingsWidget


class TestLogCollectAppLog(BaseCase):

    def test_log_collect_app_log_204(self):
        """【日志适配规范】日志收集工具查看终端应用日志"""
        widget = SettingsWidget()

        # Step 1: 点击【日志收集工具】左侧导航栏【应用日志】
        widget.open_settings_by_menu()
        # Step 2: 点击【应用列表】，依次选择、"终端"
        widget.run_cmd("deepin-terminal")
        # Step 3: 进行【级别】切换
        widget.run_cmd(
            "journalctl _COMM=deepin-terminal --priority=info --no-pager"
        )

        # Expected: 进入【应用日志】界面
        # Expected: 选择成功
        # Expected: 存在对应级别的日志信息

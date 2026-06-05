#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestDeleteWorkspace(BaseCase):

    def test_delete_workspace_183(self):
        """删除工作区"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，鼠标移动到工作区标签
        widget.run_cmd("deepin-terminal")
        # Step 2: 点击x按钮
        widget.close_current_tab()
        # Step 3: 打开终端并创建很多工作区后，使用快捷键Ctrl+Shift+W，查看软件显示
        widget.new_tab_by_plus_button()
        widget.hot_key("ctrl+shift+w")
        # Step 4: 打开终端并创建多个分屏，使用快捷键Ctrl+D，查看软件显示
        widget.horizontal_split_by_menu()
        widget.hot_key("ctrl+d")
        # Step 5: 打开终端并创建很多工作区后，点击右键－关闭工作区，查看软件显示
        widget.new_tab_by_plus_button()
        widget.close_current_tab()

        # Expected: 工作区名称旁会显示x按钮
        # Expected: 删除当前的工作区，终端直接退出
        # Expected: 软件会关闭其他的工作区
        # Expected: 软件会自动关闭当前的分屏
        # Expected: 软件会自动关闭当前的工作区

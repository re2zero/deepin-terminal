#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestDeleteCommand(BaseCase):

    def test_delete_command_163(self):
        """删除"""
        widget = CustomCommandWidget()

        # Step 1: 自定义列表任选某自定义命令，点击编辑
        widget.click_edit_button()
        # Step 2: 点击删除命令，在弹框界面点击确定
        widget.click_delete_command()
        # Step 3: 点击删除命令，在弹框界面取消
        widget.click_cancel_in_dialog()

        # Expected: 弹出编辑窗口
        # Expected: 成功删除此自定义命令；列表中下一个自定义命令上移，顺序正常改变
        # Expected: 删除失败，列表信息未变

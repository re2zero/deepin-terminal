#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestTabMessageNotification(BaseCase):

    def test_tab_message_notification_149(self):
        """标签页消息提醒"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，新建多个标签页，选中其中一个标签页，检查各个标签页名称显示
        widget.new_tab_by_plus_button()
        # Step 2: 在其中一个标签页执行命令，然后切换到其他标签页，等到命令完成
        widget.run_cmd('echo test')
        # Step 3: 此时点击标签页
        widget.click(200, 30)

        # Expected: 被选中的标签页高亮显示；
        # Expected: 执行完成之后的标签页颜色会变色，高亮显示，提醒其他标签页任务已经完成
        # Expected: 标签页自动消除标签上的提醒色

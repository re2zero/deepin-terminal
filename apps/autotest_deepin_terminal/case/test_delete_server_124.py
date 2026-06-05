#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 删除服务器
ID: 124
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestDeleteServer(BaseCase):

    def test_delete_server_124(self):
        """删除服务器"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在服务器列表中任意选中一个，点击编辑按钮，查看软件显示
        widget.click_edit_server()
        time.sleep(0.5)
        # Step 2: 在服务器对话框中点击高级选项，并点击删除服务器，查看软件显示
        widget.click_advanced_options()
        time.sleep(0.5)
        # Step 3: 在弹出的确认对话框中点击取消按钮，查看对话框显示
        widget.click_cancel_button()
        time.sleep(0.5)
        # Step 4: 在弹出的确认对话框中点击右上角的x按钮，查看对话框显示
        widget.close_dialog_by_x()
        time.sleep(0.5)
        # Step 5: 在弹出的确认对话框后按ESC键，查看对话框显示
        widget.close_dialog_by_esc()
        time.sleep(0.5)
        # Step 6: 在弹出的确认对话框中按确认按钮，查看软件显示
        widget.confirm_delete_server()

        # Assertions:
        # Expected: 软件会自动弹出编辑服务器窗口
        # Expected: 软件会弹出确认对话框：确认删除服务器？
        # Expected: 对话框会自动消失
        # Expected: 对话框会自动消失
        # Expected: 对话框会自动消失
        # Expected: 软件会自动从服务器列表中删除该服务器

#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 服务器名称
ID: 143
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestServerNameInput(BaseCase):

    def test_server_name_input_143(self):
        """服务器名称"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在弹出添加服务器窗口后，直接点击取消按钮，查看软件显示
        widget.click_cancel_button()
        time.sleep(0.5)
        # Step 2: 再弹出添加服务器窗口后，直接点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 3: 在弹出添加服务器窗口后，点击右上角的&times;按钮，查看软件显示
        widget.close_dialog_by_x()
        time.sleep(0.5)
        # Step 4: 在弹出添加服务器窗口后，按ESC键，查看软件显示
        widget.close_dialog_by_esc()
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的服务器名输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_name("阿里快圣诞节")
        time.sleep(0.5)
        # Step 6: 在添加服务器窗口的服务器名输入框中输入：asdfkad，查看软件显示
        widget.input_server_name("asdfkad")
        time.sleep(0.5)
        # Step 7: 在添加服务器窗口的服务器名输入框中输入：adkj!@#，查看软件显示
        widget.input_server_name("adkj!@#")
        time.sleep(0.5)
        # Step 8: 在添加服务器窗口的服务器名输入框中输入：超长字符，查看软件显示
        widget.input_server_name("超长字符" * 50)
        time.sleep(0.5)
        # Step 9: 在添加服务器窗口的服务器名输入框中输入：特殊字符，查看软件显示
        widget.input_server_name("!@#$%^&*()")
        time.sleep(0.5)

        # Assertions:
        # Expected: 添加服务器窗口会自动退出
        # Expected: 添加服务器窗口会自动退出
        # Expected: 添加服务器窗口会自动退出
        # Expected: 添加服务器窗口会自动退出
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，超过窗口宽度在服务器列表中以....显示
        # Expected: 可以正常输入，并显示正确

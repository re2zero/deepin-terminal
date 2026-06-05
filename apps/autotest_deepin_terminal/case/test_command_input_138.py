#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 命令
ID: 138
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestCommandInput(BaseCase):

    def test_command_input_138(self):
        """命令"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器窗口的命令输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_command("阿里快圣诞节")
        time.sleep(0.5)
        # Step 2: 在添加服务器窗口的命令输入框中输入：asdfkad，查看软件显示
        widget.input_server_command("asdfkad")
        time.sleep(0.5)
        # Step 3: 在添加服务器窗口的命令输入框中输入：adkj!@#，查看软件显示
        widget.input_server_command("adkj!@#")
        time.sleep(0.5)
        # Step 4: 在添加服务器窗口的命令输入框中输入：超长字符，查看软件显示
        widget.input_server_command("超长字符" * 50)
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的命令输入框中输入：特殊字符，查看软件显示
        widget.input_server_command("!@#$%^&*()")
        time.sleep(0.5)
        # Step 6: 在命令输入错误后，连接服务器时，查看软件显示
        widget.input_server_command("ls")
        time.sleep(0.5)
        # Step 7: 在命令输入正确后如:ls，连接服务器时，查看软件显示
        widget.input_server_command("ls")
        time.sleep(0.5)

        # Assertions:
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 软件连接不上
        # Expected: 连接服务器成功后，并直接输出命令ls

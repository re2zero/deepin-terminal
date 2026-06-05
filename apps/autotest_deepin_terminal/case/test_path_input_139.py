#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 路径
ID: 139
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestPathInput(BaseCase):

    def test_path_input_139(self):
        """路径"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器窗口的路径输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_path("阿里快圣诞节")
        time.sleep(0.5)
        # Step 2: 在添加服务器窗口的路径输入框中输入：asdfkad，查看软件显示
        widget.input_server_path("asdfkad")
        time.sleep(0.5)
        # Step 3: 在添加服务器窗口的路径输入框中输入：adkj!@#，查看软件显示
        widget.input_server_path("adkj!@#")
        time.sleep(0.5)
        # Step 4: 在添加服务器窗口的路径输入框中输入：超长字符，查看软件显示
        widget.input_server_path("超长字符" * 50)
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的路径输入框中输入：特殊字符，查看软件显示
        widget.input_server_path("!@#$%^&*()")
        time.sleep(0.5)
        # Step 6: 在路径中输入错误的路径后，然后连接服务器时，查看软件显示
        widget.input_server_path("/home")
        time.sleep(0.5)
        # Step 7: 在路径中输入正确的路径后如：/home，然后连接服务器时，查看软件显示
        widget.input_server_path("/home")
        time.sleep(0.5)

        # Assertions:
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 路径识别错误，不会进行跳转
        # Expected: 路径识别正确，服务器登陆成功后并自动跳转到/home目录

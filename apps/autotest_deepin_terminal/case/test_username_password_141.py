#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 用户名密码
ID: 141
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestUsernamePassword(BaseCase):

    def test_username_password_141(self):
        """用户名密码"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器窗口的用户名输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_username("阿里快圣诞节")
        time.sleep(0.5)
        # Step 2: 在添加服务器窗口的用户名输入框中输入：asdfkad，查看软件显示
        widget.input_server_username("asdfkad")
        time.sleep(0.5)
        # Step 3: 在添加服务器窗口的用户名输入框中输入：adkj!@#，查看软件显示
        widget.input_server_username("adkj!@#")
        time.sleep(0.5)
        # Step 4: 在添加服务器窗口的用户名输入框中输入：超长字符，查看软件显示
        widget.input_server_username("超长字符" * 50)
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的用户名输入框中输入：特殊字符，查看软件显示
        widget.input_server_username("!@#$%^&*()")
        time.sleep(0.5)
        # Step 6: 在添加服务器窗口的密码输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_password("阿里快圣诞节")
        time.sleep(0.5)
        # Step 7: 在添加服务器窗口的密码输入框中输入：asdfkad，查看软件显示
        widget.input_server_password("asdfkad")
        time.sleep(0.5)
        # Step 8: 在添加服务器窗口的密码输入框中输入：adjk!@#，查看软件显示
        widget.input_server_password("adjk!@#")
        time.sleep(0.5)
        # Step 9: 在密码输入框后面有一个显示密码按钮，点击一下，查看密码显示
        widget.click_show_password()
        time.sleep(0.5)

        # Assertions:
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 不能输入汉字
        # Expected: 可以正输入，以加密方式显示
        # Expected: 可以正常输入，以加密方式显示
        # Expected: 密码会以明文方式显示

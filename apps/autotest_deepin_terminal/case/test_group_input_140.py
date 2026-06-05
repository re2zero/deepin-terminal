#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 分组
ID: 140
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestGroupInput(BaseCase):

    def test_group_input_140(self):
        """分组"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器对话框中点击高级选项，查看对话框显示
        widget.click_advanced_options()
        time.sleep(0.5)
        # Step 2: 在添加服务器窗口的分组输入框中输入：阿里快圣诞节，查看软件显示
        widget.input_server_group("阿里快圣诞节")
        time.sleep(0.5)
        # Step 3: 在添加服务器窗口的分组输入框中输入：asdfkad，查看软件显示
        widget.input_server_group("asdfkad")
        time.sleep(0.5)
        # Step 4: 在添加服务器窗口的分组输入框中输入：adkj!@#，查看软件显示
        widget.input_server_group("adkj!@#")
        time.sleep(0.5)
        # Step 5: 在添加服务器窗口的分组输入框中输入：超长字符，查看软件显示
        widget.input_server_group("超长字符" * 50)
        time.sleep(0.5)
        # Step 6: 在添加服务器窗口的分组输入框中输入：特殊字符，查看软件显示
        widget.input_server_group("!@#$%^&*()")
        # Step 7: 假如当前软件中没有任何分组，然后新建一个分组，查看软件显示
        widget.input_server_group("test_group")
        time.sleep(0.5)
        # Step 8: 假如当前软件中已经有分组，然后填写一个已经存在的分组名，查看软件显示
        widget.input_server_group("test_group")
        time.sleep(0.5)

        # Assertions:
        # Expected: 窗口会自动向下展开，并显示高级选项
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 可以正常输入，并显示正确
        # Expected: 软件会新建一个分组，并将当前的服务器添加到该分组中
        # Expected: 软件会将当前的服务器添加到该分组中

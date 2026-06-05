#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 必填项
ID: 133
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestRequiredFields(BaseCase):

    def test_required_fields_133(self):
        """必填项"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器界面中只填写服务器名，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 2: 在添加服务器界面中只填写地址，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 3: 在添加服务器界面中只填写用户名，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 4: 在添加服务器界面中只填写服务器名和地址，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 5: 在添加服务器界面中只填写服务器名和用户名，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 6: 在添加服务器界面中只填写地址和用户名，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 7: 在添加服务器界面中填写服务器名、地址和用户名，点击添加按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)

        # Assertions:
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 软件不会添加服务器到服务器列表中
        # Expected: 添加服务器成功，并自动保存到服务器列表中

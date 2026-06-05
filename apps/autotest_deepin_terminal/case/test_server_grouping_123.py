#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 服务器分组
ID: 123
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestServerGrouping(BaseCase):

    def test_server_grouping_123(self):
        """服务器分组"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 在添加服务器时填写一个新的分组，查看服务器列表显示
        widget.input_server_group("new_group")
        time.sleep(0.5)
        # Step 2: 在添加服务器时填写一个已经存在的分组，查看服务器列表显示
        widget.input_server_group("existing_group")
        time.sleep(0.5)
        # Step 3: 在修改服务器时填写一个新组，查看服务器列表显示
        widget.click_edit_server()
        time.sleep(0.5)
        widget.input_server_group("another_new_group")
        time.sleep(0.5)
        # Step 4: 在修改服务器时填写一个已存在组，查看服务器列表显示
        widget.click_edit_server()
        time.sleep(0.5)
        widget.input_server_group("existing_group")
        time.sleep(0.5)
        # Step 5: 在修改服务器时，将一个组中的服务器修改到另一个组中，查看服务器列表显示
        widget.click_edit_server()
        time.sleep(0.5)
        widget.input_server_group("another_new_group")
        time.sleep(0.5)
        # Step 6: 假如当前分组只有一个服务器，然后删除分组、修改分组、删除该服务器，查看分组显示
        widget.input_server_group("test_group")
        time.sleep(0.5)
        widget.click_delete_server()
        time.sleep(0.5)
        # Step 7: 在新增和修改分组时，查看分组服务器数量显示
        widget.input_server_group("test_group")
        time.sleep(0.5)

        # Assertions:
        # Expected: 软件会自动创建一个新组，并将该服务器添加到该组中
        # Expected: 软件会自动将该服务器添加到以存在的分组中
        # Expected: 软件会自动创建一个新组，并将该服务器添加到该组中
        # Expected: 软件会自动将该服务器添加到以存在的分组中
        # Expected: 该服务器会从当前服务器消失，并跳转到另一个服务器中
        # Expected: 组中没有服务器时，该分组会自动删除
        # Expected: 服务器数量显示正确

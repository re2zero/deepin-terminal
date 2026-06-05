#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
TestCase: 服务器窗口
ID: 121
"""
import time
from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.remote_management_widget import RemoteManagementWidget


class TestServerWindow(BaseCase):

    def test_server_window_121(self):
        """服务器窗口"""
        widget = RemoteManagementWidget()
        time.sleep(0.5)
        # Step 1: 打开终端，在终端中点击右键，查看是否有远程管理显示
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 2: 在终端的右键菜单中点击远程管理，查看软件显示
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 3: 打开终端后点击右上角的主菜单-远程管理，查看软件显示
        widget.open_remote_management_by_menu()
        time.sleep(0.5)
        # Step 4: 软件弹出添加远程服务器窗口后，点击除添加窗口外软件其他的地方
        widget.hide_remote_management()
        time.sleep(0.5)
        # Step 5: 打开终端使用快捷键alt+del查看软件显示
        widget.open_remote_management_by_shortcut()
        time.sleep(0.5)
        # Step 6: 软件已经弹出远程服务器窗口，使用快捷键alt+del，查看软件显示
        widget.open_remote_management_by_shortcut()
        time.sleep(0.5)
        # Step 7: 在弹出添加服务器窗口后，点击添加服务器按钮，查看软件显示
        widget.click_add_server_button()
        time.sleep(0.5)
        # Step 8: 在弹出添加服务器窗口后，点击右上角的x，查看窗口显示
        widget.close_dialog_by_x()
        time.sleep(0.5)
        # Step 9: 在弹出添加服务器窗口后，按ESC键，查看窗口显示
        widget.close_dialog_by_esc()
        time.sleep(0.5)

        # Assertions:
        # Expected: 有远程管理菜单显示
        # Expected: 软件的右侧会自动弹出窗口显示可以添加远程服务器
        # Expected: 软件的右侧会自动弹出窗口显示可以添加远程服务器
        # Expected: 添加远程服务器窗口会自动收回
        # Expected: 软件会自动弹出添加远程服务器窗口
        # Expected: 添加远程服务窗口会自动退出
        # Expected: 软件会自动弹出添加服务器窗口
        # Expected: 窗口会自动关闭
        # Expected: 窗口会自动关闭

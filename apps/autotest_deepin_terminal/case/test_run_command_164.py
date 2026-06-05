#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestRunCommand(BaseCase):

    def test_run_command_164(self):
        """运行"""
        widget = CustomCommandWidget()

        # Step 1: 新建自定义命令:名称：深度音乐  命令：deepin-music    快捷键：crtl+p（或者无）点击添加
        widget.click_add_command_button()
        # Step 2: 终端中键盘敲入ctrl+p（有快捷键的情况下）
        widget.input_command_shortcut("ctrl+p")
        # Step 3: 进入终端自定义命令列表，点击名为深度音乐的命令
        widget.hide_custom_command()
        # Step 4: 修改命令为sayonara（未安装的软件或者服务），修改名称为测试，保存
        widget.click_add_button_in_dialog()
        # Step 5: 终端中键盘敲入ctrl+p（有快捷键的情况下）
        widget.input_command_shortcut("ctrl+p")
        # Step 6: 进入终端自定义命令列表，点击名为测试的命令
        widget.hide_custom_command()
        # Step 7: 进入远程服务器后，点击自定义命令，查看软件显示
        widget.click_add_command_button()

        # Expected: 成功添加到自定义命令列表
        # Expected: 成功开启深度音乐
        # Expected: 系统成功开启深度音乐
        # Expected: 修改成功
        # Expected: 不会开启相应服务或者软件
        # Expected: 没有开启服务或这软件，终端有相应信息提示
        # Expected: 在远程服务器上也可以正常运行自定义命令

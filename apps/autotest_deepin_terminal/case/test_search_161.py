#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.custom_command_widget import CustomCommandWidget


class TestSearch(BaseCase):

    def test_search_161(self):
        """搜索"""
        widget = CustomCommandWidget()

        # Step 1: 终端右键自定义命令
        widget.open_custom_command_by_menu()
        # Step 2: 不输入任何字符直接enter搜索
        widget.press_search_enter()
        # Step 3: 输入只有命令名称字符的搜索字符
        widget.input_command_name("test_command")
        # Step 4: 输入只含有命令内容字符的搜索字符
        widget.input_command_text("echo hello")
        # Step 5: 输入只含有命令快捷键的搜索字符
        widget.input_command_text("echo hello")
        # Step 6: 分别单独搜索同一字母的大写和小写
        widget.input_search_text("T")
        # Step 7: 搜索后点击向前箭头
        widget.click_search_back()
        # Step 8: 分别对自定义命令的命令名称和具体命令进行搜索
        widget.input_search_text("test")

        # Expected: 右侧开启自定义命令栏
        # Expected: 搜索失败，必须输入相应字符
        # Expected: 可以按命令名称搜索
        # Expected: 可以按命令内容进行搜索
        # Expected: 可以按命令快捷键进行搜索
        # Expected: 两次搜索结果完全一致，搜索不区分大小写
        # Expected: 回到自定义命令列表
        # Expected: 都能搜索到，只要有一项匹配即可

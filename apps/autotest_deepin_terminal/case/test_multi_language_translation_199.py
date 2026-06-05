#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.main_menu_widget import MainMenuWidget


class TestMultiLanguageTranslation(BaseCase):

    def test_multi_language_translation_199(self):
        """多语言界面翻译"""
        widget = MainMenuWidget()

        # Step 1: 检查中文、英文、繁体、正体、维语、藏语语言系统下，终端各个界面翻译是否正常
        widget.click_main_menu()

        # Expected: 翻译显示正常

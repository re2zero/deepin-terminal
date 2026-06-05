#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestDragUploadFile(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_drag_upload_file_146(self):
        """连接服务器后拖拽文件上传"""
        pass

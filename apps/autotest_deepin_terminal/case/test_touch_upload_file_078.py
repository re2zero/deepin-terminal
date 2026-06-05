#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pytest
from apps.autotest_deepin_terminal.case.base_case import BaseCase


class TestTouchUploadFile(BaseCase):

    @pytest.mark.skip(reason="skip-触摸操作无法自动化")
    def test_touch_upload_file_078(self):
        """触摸屏连接服务器上传文件"""
        pass

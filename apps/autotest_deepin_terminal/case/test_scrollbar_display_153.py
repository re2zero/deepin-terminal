#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from apps.autotest_deepin_terminal.case.base_case import BaseCase
from apps.autotest_deepin_terminal.widget.workspace_widget import WorkspaceWidget


class TestScrollbarDisplay(BaseCase):

    def test_scrollbar_display_153(self):
        """滚动条显示"""
        widget = WorkspaceWidget()

        # Step 1: 打开终端，检查内容够屏幕显示时，是否有滚动条
        widget.run_cmd("deepin-terminal")
        # Step 2: 修改窗口宽度，让终端输出一长串内容，检查是否有横向滚动条
        widget.run_cmd("seq 1 1000 | while read i; do echo $i; done")
        # Step 3: 修改窗口高度：减小高度，终端输出一段内容，检查是否有纵向滚动条
        widget.restore_window()
        widget.run_cmd("yes 'aaaaaa' | head -200")
        # Step 4: 增加窗口高度，终端内容够显示完整，检查是否有滚动条
        widget.maximize_window()
        # Step 5: 再次缩小窗口高度
        widget.restore_window()
        # Step 6: 鼠标移动到右侧的滚动条
        widget.click(700, 400)
        # Step 7: 使用shift+pageup/pagedown
        widget.hot_key("shift+pageup")
        widget.hot_key("shift+pagedown")

        # Expected: 没有显示滚动条
        # Expected: 没有横向滚动条
        # Expected: 出现纵向滚动条
        # Expected: 滚动条不会显示
        # Expected: 滚动条出现
        # Expected: 滚动条放大
        # Expected: 可以上下滚动屏幕

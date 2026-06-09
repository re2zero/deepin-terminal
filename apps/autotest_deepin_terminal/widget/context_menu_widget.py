#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for right-click context menu functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from apps.autotest_deepin_terminal.widget.menu_utils import context_menu_click
from src import log


@log
class ContextMenuWidget(BaseWidget):
    """Widget methods for the right-click context menu functionality."""

    # === Right-click menu operations ===

    def open_context_menu(self, x=400, y=300):
        """Open right-click context menu at given coordinates."""
        self.right_click(x, y)
        import time
        time.sleep(0.3)

    def click_context_menu_item(self, menu_item, x=400, y=300):
        context_menu_click(menu_item, click_x=x, click_y=y)

    def click_open_in_file_manager(self):
        """Click 'Open in file manager' from context menu."""
        self.click_context_menu_item("在文件管理器中打开")

    def click_horizontal_split(self):
        """Click 'Horizontal split' from context menu."""
        self.click_context_menu_item("横向分屏")

    def click_vertical_split(self):
        """Click 'Vertical split' from context menu."""
        self.click_context_menu_item("纵向分屏")

    def click_close_workspace(self):
        """Click 'Close workspace' from context menu."""
        self.click_context_menu_item("关闭工作区")

    def click_new_tab(self):
        """Click 'New tab' from context menu."""
        self.click_context_menu_item("新建标签页")

    def click_fullscreen(self):
        """Click 'Fullscreen' from context menu."""
        self.click_context_menu_item("全屏")

    def click_search(self):
        """Click 'Search' from context menu."""
        self.click_context_menu_item("查找")

    def click_encoding(self):
        """Click 'Encoding' from context menu."""
        self.click_context_menu_item("编码")

    def click_custom_command(self):
        """Click 'Custom command' from context menu."""
        self.click_context_menu_item("自定义命令")

    def click_remote_management(self):
        """Click 'Remote management' from context menu."""
        self.click_context_menu_item("远程管理")

    def click_settings(self):
        """Click 'Settings' from context menu."""
        self.click_context_menu_item("设置")

    def click_paste(self):
        """Click 'Paste' from context menu."""
        self.click_context_menu_item("粘贴")

    def click_copy(self):
        """Click 'Copy' from context menu."""
        self.click_context_menu_item("复制")

    def click_open_link(self):
        """Click 'Open link' from context menu."""
        self.click_context_menu_item("打开链接")

    def click_copy_link(self):
        """Click 'Copy link' from context menu."""
        self.click_context_menu_item("复制链接")

    def click_open_file(self):
        """Click 'Open' from context menu (when file is selected)."""
        self.click_context_menu_item("打开")

    def click_search_in_selection(self):
        """Click 'Search' from context menu (when text is selected)."""
        self.click_context_menu_item("搜索")

    def click_rename_title(self):
        """Click 'Rename title' from context menu."""
        self.click_context_menu_item("重命名标题")

    # === Alt+M shortcut menu ===

    def open_menu_by_alt_m(self):
        """Open context menu using Alt+M shortcut."""
        self.hot_key("alt+m")
        import time
        time.sleep(0.3)

    def close_context_menu_by_esc(self):
        """Close context menu by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

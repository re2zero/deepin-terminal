#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for remote management functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class RemoteManagementWidget(BaseWidget):
    """Widget methods for the remote management functionality."""

    # === Open remote management panel ===

    def open_remote_management_by_menu(self):
        """Open remote management panel via right-click menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("远程管理")
        time.sleep(0.5)

    def open_remote_management_by_main_menu(self):
        """Open remote management via main menu."""
        self.dog.element_click("DTitlebarDWindowOptionButton")
        import time
        time.sleep(0.3)
        self.dog.element_click("远程管理")
        time.sleep(0.5)

    def open_remote_management_by_shortcut(self):
        """Open remote management using Alt+Del shortcut."""
        self.hot_key("alt+del")
        import time
        time.sleep(0.5)

    # === Hide panel ===

    def hide_remote_management(self):
        """Hide remote management panel by clicking terminal area."""
        self.click(400, 400)
        import time
        time.sleep(0.3)

    def hide_by_esc(self):
        """Hide remote management panel by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    # === Add server ===

    def click_add_server_button(self):
        """Click the add server button."""
        self.dog.element_click("添加服务器")
        import time
        time.sleep(0.3)

    def input_server_name(self, name):
        """Type server name in the add server dialog."""
        self.input_message(name)
        import time
        time.sleep(0.3)

    def input_server_address(self, address):
        """Type server address."""
        self.input_message(address)
        import time
        time.sleep(0.3)

    def input_server_port(self, port):
        """Type server port."""
        self.input_message(port)
        import time
        time.sleep(0.3)

    def input_server_username(self, username):
        """Type server username."""
        self.input_message(username)
        import time
        time.sleep(0.3)

    def input_server_password(self, password):
        """Type server password."""
        self.input_message(password)
        import time
        time.sleep(0.3)

    def click_show_password(self):
        """Click show password button."""
        self.dog.element_click("显示密码")
        import time
        time.sleep(0.3)

    def input_server_group(self, group):
        """Type server group name."""
        self.input_message(group)
        import time
        time.sleep(0.3)

    def input_server_path(self, path):
        """Type server login path."""
        self.input_message(path)
        import time
        time.sleep(0.3)

    def input_server_command(self, command):
        """Type server login command."""
        self.input_message(command)
        import time
        time.sleep(0.3)

    def click_advanced_options(self):
        """Click advanced options to expand additional fields."""
        self.dog.element_click("高级选项")
        import time
        time.sleep(0.3)

    def select_server_encoding(self, encoding):
        """Select encoding for server connection."""
        self.dog.element_click(encoding)
        import time
        time.sleep(0.3)

    def select_backspace_key(self, key_option):
        """Select backspace key behavior."""
        self.dog.element_click(key_option)
        import time
        time.sleep(0.3)

    def select_delete_key(self, key_option):
        """Select delete key behavior."""
        self.dog.element_click(key_option)
        import time
        time.sleep(0.3)

    def click_add_button(self):
        """Click Add button in add server dialog."""
        self.dog.element_click("添加")
        import time
        time.sleep(0.3)

    def click_save_button(self):
        """Click Save button in edit server dialog."""
        self.dog.element_click("保存")
        import time
        time.sleep(0.3)

    def click_cancel_button(self):
        """Click Cancel button in dialog."""
        self.dog.element_click("取消")
        import time
        time.sleep(0.3)

    def close_dialog_by_x(self):
        """Close dialog by clicking X button."""
        self.dog.element_click("DTitlebarDWindowCloseButton")
        import time
        time.sleep(0.3)

    def close_dialog_by_esc(self):
        """Close dialog by pressing ESC."""
        self.press_key("Escape")
        import time
        time.sleep(0.3)

    # === Edit/Delete server ===

    def click_edit_server(self):
        """Click edit button for selected server."""
        self.dog.element_click("编辑")
        import time
        time.sleep(0.3)

    def click_delete_server(self):
        """Click delete server in the edit dialog."""
        self.dog.element_click("删除服务器")
        import time
        time.sleep(0.3)

    def confirm_delete_server(self):
        """Confirm server deletion."""
        self.dog.element_click("确定")
        import time
        time.sleep(0.3)

    def cancel_delete_server(self):
        """Cancel server deletion."""
        self.dog.element_click("取消")
        import time
        time.sleep(0.3)

    # === Connect server ===

    def connect_server(self, server_name):
        """Click on a server to connect."""
        self.dog.element_click(server_name)
        import time
        time.sleep(1.0)

    # === Search ===

    def input_search_text(self, text):
        """Type search text in server search box."""
        self.input_message(text)
        import time
        time.sleep(0.3)

    def clear_search(self):
        """Clear search by clicking delete button."""
        # Click the delete/clear button next to search
        self.hot_key("BackSpace")
        import time
        time.sleep(0.3)

    # === Server group navigation ===

    def enter_server_group(self, group_name):
        """Enter a server group by clicking or pressing Enter."""
        self.dog.element_click(group_name)
        import time
        time.sleep(0.3)

    def navigate_servers_by_arrow(self):
        """Navigate server list using arrow keys."""
        import time
        self.press_key("Down")
        time.sleep(0.2)
        self.press_key("Up")
        time.sleep(0.2)

    def tab_to_search_box(self):
        """Tab to search box in remote management panel."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    def tab_to_add_button(self):
        """Tab from server list to add server button."""
        self.press_key("Tab")
        import time
        time.sleep(0.2)

    # === Upload/Download ===

    def click_upload_file(self):
        """Click upload file in right-click menu on remote session."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("上传文件")
        time.sleep(0.5)

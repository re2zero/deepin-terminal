#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
Widget methods for settings dialog functionality.
"""

from apps.autotest_deepin_terminal.widget.base_widget import BaseWidget
from src import log


@log
class SettingsWidget(BaseWidget):
    """Widget methods for the settings functionality."""

    # === Open settings ===

    def open_settings_by_menu(self):
        """Open settings dialog via main menu."""
        self.dog.element_click("DTitlebarDWindowOptionButton")
        import time
        time.sleep(0.3)
        self.dog.element_click("设置")
        time.sleep(0.5)

    def open_settings_by_right_click(self):
        """Open settings dialog via right-click context menu."""
        self.right_click(400, 300)
        import time
        time.sleep(0.3)
        self.dog.element_click("设置")
        time.sleep(0.5)

    def close_settings_by_esc(self):
        """Close settings dialog by pressing ESC."""
        self.press_key("Escape")

    def close_settings_by_x(self):
        """Close settings dialog by clicking X button."""
        self.dog.element_click("DTitlebarDWindowCloseButton")

    # === Basic settings ===

    def click_basic_settings(self):
        """Click basic settings tab in left sidebar."""
        self.dog.element_click("基础设置")

    def set_opacity(self, value):
        """Set opacity slider to given value (0.2-1.0)."""
        import time
        time.sleep(0.3)
        # Use keyboard to adjust since AT-SPI slider interaction varies
        current = 1.0
        steps = int((current - value) / 0.1)
        for _ in range(steps):
            self.press_key("Left")

    def select_font(self, font_name):
        """Select a font from font dropdown (AT-SPI role: combo box)."""
        self.dog.element_click("Noto Sans Mono")
        import time
        time.sleep(0.3)
        self.dog.element_click(font_name)
        time.sleep(0.3)

    def increase_font_size(self):
        """Click font size increase button."""
        self.dog.element_click("+")

    def decrease_font_size(self):
        """Click font size decrease button."""
        self.dog.element_click("-")

    # === Shortcut settings ===

    def click_shortcut_settings(self):
        """Click shortcut settings tab in left sidebar."""
        self.dog.element_click("快捷键")

    def click_shortcut_item(self, shortcut_name):
        """Click a shortcut entry to modify it."""
        self.dog.element_click(shortcut_name)

    def input_new_shortcut(self, keys):
        """Input new shortcut key combination."""
        import time
        time.sleep(0.3)
        self.hot_key(keys)
        time.sleep(0.3)

    # === Advanced settings ===

    def click_advanced_settings(self):
        """Click advanced settings tab in left sidebar."""
        self.dog.element_click("高级设置")

    def switch_cursor_style(self, style_index=0):
        """Switch cursor style (0=block, 1=|, 2=_)."""
        import time
        self.dog.element_click("光标风格")
        time.sleep(0.3)
        for _ in range(style_index):
            self.press_key("Right")
        self.press_key("Return")
        time.sleep(0.3)

    def toggle_cursor_blink(self):
        """Toggle cursor blink checkbox."""
        self.dog.element_click("光标闪烁")

    def toggle_scroll_on_key(self):
        """Toggle scroll on keypress checkbox."""
        self.dog.element_click("按键时滚动")

    def toggle_scroll_on_output(self):
        """Toggle scroll on output checkbox."""
        self.dog.element_click("输出时滚动")

    def select_startup_mode(self, mode):
        """Select startup window mode from dropdown (AT-SPI combo box)."""
        self.dog.element_click("正常窗口")
        import time
        time.sleep(0.3)
        self.dog.element_click(mode)
        time.sleep(0.3)

    def toggle_blur_background(self):
        """Toggle blur background checkbox."""
        self.dog.element_click("背景模糊")

    def toggle_hide_quake_on_lost_focus(self):
        """Toggle hide quake window on lost focus checkbox."""
        self.dog.element_click("丢失焦点后自动隐藏雷神窗口")

    def toggle_auto_copy_on_select(self):
        """Toggle auto copy to clipboard on text selection checkbox."""
        self.dog.element_click("选中文字时自动复制到剪贴板")

    def select_shell(self, shell_name):
        """Select shell from shell configuration dropdown (AT-SPI combo box)."""
        self.dog.element_click("$SHELL")
        import time
        time.sleep(0.3)
        self.dog.element_click(shell_name)
        time.sleep(0.3)

    def toggle_disable_ctrl_s_q(self):
        """Toggle disable Ctrl+S and Ctrl+Q checkbox."""
        self.dog.element_click("禁用Ctrl+S和Ctrl+Q控制")

    def click_restore_defaults(self):
        """Click restore defaults button."""
        self.dog.element_click("ContentSettingsResetButton")

    def tab_to_restore_defaults(self):
        """Tab to restore defaults button and click it."""
        import time
        while True:
            self.press_key("Tab")
            time.sleep(0.2)
            if self.dog.is_element_exist("恢复所有"):
                break
        self.press_key("Return")
        time.sleep(0.3)

    # === Tab navigation in settings ===

    def tab_navigate_settings(self, count=1):
        """Press Tab key N times in settings dialog."""
        import time
        for _ in range(count):
            self.press_key("Tab")
            time.sleep(0.2)

    def tab_navigate_settings_reverse(self, count=1):
        """Press Shift+Tab N times in settings dialog."""
        import time
        for _ in range(count):
            self.hot_key("Shift+Tab")
            time.sleep(0.2)

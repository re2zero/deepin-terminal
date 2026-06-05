# deepin-terminal AT-SPI Element Reference

> Captured from live AT-SPI tree on 2026-06-04.
> Environment: X11, DISPLAY=:0, AT_SPI_BUS_ADDRESS=unix:path=/run/user/1000/at-spi/bus_0

## Main Window (frame: "DMainWindow")

### Titlebar (panel: "DMainWindowTitlebar")

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Main menu button | button | `DTitlebarDWindowOptionButton` | Hamburger menu, top-left |
| Minimize | button | `DTitlebarDWindowMinButton` | |
| Maximize | button | `DTitlebarDWindowMaxButton` | |
| Quit fullscreen | button | `DTitlebarDWindowQuitFullscreenButton` | Only visible in fullscreen |
| Close | button | `DTitlebarDWindowCloseButton` | |
| App icon | button | `DTitlebarIconLabel` | Top-left icon |

### Tab Bar

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Tab list | page tab list | (dynamic) | Contains current path as name |
| Tab item | page tab | (dynamic) | Tab title = current working directory path |
| Add tab button | button | `DTabBarAddButton` | "+" button |
| Scroll left | button | `向左滚动` | Appears when many tabs |
| Scroll right | button | `向右滚动` | Appears when many tabs |
| Unnamed button 1 | button | "" | (unknown purpose, empty name) |
| Unnamed button 2 | button | "" | (unknown purpose, empty name) |

### Terminal Content Area

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Terminal content | layered pane | "" | Contains terminal rendering |
| Scroll bar | scroll bar | "" | Terminal scrollbar |

### Search Bar (Ctrl+Alt+F)

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Search input | text | `DLineEditChildLineEdit` | Text input field |
| Search button 1 | button | "" | (unknown, likely up/down) |
| Search button 2 | button | "" | (unknown, likely up/down) |
| Search size label | label | `大小: W x H` | Popup label showing match size |

## Main Menu (popup menu: "DTitlebarMainMenu")

| Menu Item | AT-SPI Role | AT-SPI Name | Has Submenu |
|-----------|-------------|-------------|-------------|
| New window | menu item | `新建窗口` | No |
| Custom commands | menu item | `自定义命令` | No |
| Remote management | menu item | `远程管理` | No |
| Settings | menu item | `设置` | No |
| Theme | menu item | `主题` | Yes |
| Help | menu item | `帮助` | No |
| About | menu item | `关于` | No |
| Exit | menu item | `退出` | No |

### Theme Submenu (popup menu: "")

| Item | AT-SPI Role | AT-SPI Name | Notes |
|------|-------------|-------------|-------|
| Light | menu item | `浅色` | |
| Dark | menu item | `深色` | |
| Follow system | menu item | `跟随系统` | |
| --- separator --- | separator | "" | |
| Elementary | menu item | `Elementary` | Color theme |
| Empathy | menu item | `Empathy` | Color theme |
| Tomorrow night blue | menu item | `Tomorrow night blue` | Color theme |
| Bim | menu item | `Bim` | Color theme |
| Freya | menu item | `Freya` | Color theme |
| Hybrid | menu item | `Hybrid` | Color theme |
| Ocean dark | menu item | `Ocean dark` | Color theme |
| Deepin | menu item | `Deepin` | Color theme |
| Ura | menu item | `Ura` | Color theme |
| One light | menu item | `One light` | Color theme |
| BlackOnLightYellow | menu item | `BlackOnLightYellow` | Color theme |
| BlackOnRandomLight | menu item | `BlackOnRandomLight` | Color theme |
| BlackOnWhite | menu item | `BlackOnWhite` | Color theme |
| BreezeModified | menu item | `BreezeModified` | Color theme |
| DarkPastels | menu item | `DarkPastels` | Color theme |
| GreenOnBlack | menu item | `GreenOnBlack` | Color theme |
| Linux | menu item | `Linux` | Color theme |
| Solarized | menu item | `Solarized` | Color theme |
| SolarizedLight | menu item | `SolarizedLight` | Color theme |
| Tango | menu item | `Tango` | Color theme |
| Ubuntu | menu item | `Ubuntu` | Color theme |
| WhiteOnBlack | menu item | `WhiteOnBlack` | Color theme |
| Custom theme | menu item | `自定义主题` | Opens theme editor |

### App Theme Submenu (popup menu: "DTitlebarThemeMenu")

| Item | AT-SPI Role | AT-SPI Name |
|------|-------------|-------------|
| Light | menu item | `浅色` |
| Dark | menu item | `深色` |
| Follow system | menu item | `跟随系统` |

## Settings Dialog (dialog: "")

### Dialog Titlebar

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Settings titlebar | panel | `DSettingTitleBar` | |
| Close button | button | `DTitlebarDWindowCloseButton` | |
| Minimize | button | `DTitlebarDWindowMinButton` | |
| Maximize | button | `DTitlebarDWindowMaxButton` | |

### Left Navigation (panel: "DSettingDialogLeftFrame")

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Navigation list | list | `NavigationBar` | Left sidebar |
| Basic settings | list item | `基础设置` | |
| Interface | list item | `界面` | |
| Tab title | list item | `标签标题` | |
| Shortcuts | list item | `快捷键` | Parent category |
| Terminal shortcuts | list item | `终端` | Sub-item under Shortcuts |
| Tab shortcuts | list item | `标签页` | Sub-item under Shortcuts |
| Other shortcuts | list item | `其他` | Sub-item under Shortcuts |
| Advanced settings | list item | `高级设置` | Parent category |
| Cursor | list item | `光标` | Sub-item under Advanced |
| Scroll | list item | `滚动` | Sub-item under Advanced |
| Window | list item | `窗口` | Sub-item under Advanced |
| Shell | list item | `Shell` | Sub-item under Advanced |
| Debuginfod | list item | `Debuginfod` | Sub-item under Advanced |

### Right Content Panel (panel: "DSettingDialogRightFrame")

Structure: `DSettingDialogContentWidget` > `ContentScrollArea` > `ContentScrollAreaViewPort` > `ContentSettingsFrame`

#### Interface Section (ContentWidgetForbasic.interface)

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Font combo box | combo box | `Noto Sans Mono` | Name = current font value |
| Font size spin button | spin button | "" | |
| Row backgrounds | filler | `CustomWidgetAtContentRow3BackgroundRow0/1/2/3` | |

#### Shortcut Sections

Each shortcut entry is a `text` element inside `CustomWidgetAtContentRowNBackgroundRowM` fillers.
- Shortcuts section (terminal, tab, other): rows 0-6+ with empty text elements
- No shortcut action names visible in AT-SPI (all text elements are empty strings)

#### Advanced Sections

**Cursor (ContentWidgetForadvanced.cursor)**

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Option button box | filler | `OptionButtonBox` | Inside row 0 |
| Cursor text input | text | `OptionLineEdit` | Custom cursor text |
| Rows 2-5 | filler | `CustomWidgetAtContentRow17BackgroundRow2/3/4/5` | |

**Scroll (ContentWidgetForadvanced.scroll)**

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Scrollback spin button | spin button | "" | Inside row 0 |
| Rows 1-4 | filler | `CustomWidgetAtContentRow19BackgroundRow1/2/3/4` | |

**Window (ContentWidgetForadvanced.window)**

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Startup mode combo box | combo box | `正常窗口` | Name = current mode value |
| Rows 1-2 | filler | `CustomWidgetAtContentRow21BackgroundRow1/2` | |

**Shell (ContentWidgetForadvanced.shell)**

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Shell combo box | combo box | `$SHELL` | Name = current shell value |
| Row 1 | filler | `CustomWidgetAtContentRow23BackgroundRow1` | |

**Debuginfod (ContentWidgetForadvanced.debuginfod)**

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| URL input | text | `OptionLineEdit` | Debuginfod server URL |
| Row 0 | filler | `CustomWidgetAtContentRow25BackgroundRow0` | Toggle |

### Settings Footer

| Element | AT-SPI Role | AT-SPI Name | Notes |
|---------|-------------|-------------|-------|
| Restore defaults button | button | `ContentSettingsResetButton` | Bottom of settings |

## Known Limitations

### Right-click Context Menu (NOT in AT-SPI)

The terminal content area right-click context menu does **NOT** register with AT-SPI.
Menu items like `横向分屏`, `纵向分屏`, `在文件管理器中打开`, `查找`, `编码`, `全屏`, `新建标签页`, `关闭工作区`, `复制`, `粘贴`, `打开链接`, `复制链接`, `打开`, `搜索`, `重命名标题` must be accessed via:
- Coordinate-based clicking (`self.right_click(x, y)`)
- OCR/VLM-based element detection
- Keyboard shortcuts as alternatives

### Empty-named Elements

Several buttons and fillers have empty string names (`""`). These cannot be reliably targeted by name and require:
- Index-based access
- Coordinate-based interaction
- Role-based filtering combined with position

## AT-SPI Access Pattern

```python
import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

desktop = Atspi.get_desktop(0)
for i in range(desktop.get_child_count()):
    app = desktop.get_child_at_index(i)
    if app.get_name() == 'deepin-terminal':
        # iterate windows, dialogs, popup menus...
        pass
```

Required environment variables:
- `DISPLAY=:0`
- `AT_SPI_BUS_ADDRESS=unix:path=/run/user/1000/at-spi/bus_0`
- `QT_ACCESSIBILITY=1`
- `QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1`

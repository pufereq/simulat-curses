## 0.5.0-alpha.1 (2023-10-22)

### Feat

- **menu_widget.py**: make `self.MENU_SIZE` dependent on widget's size
- **container.py**: add `description` field to `Container` class constructor
- **menu_widget.py**: add `_display_info` method
- **menu_widget.py**: add vim keybindings (`j` (down) & `k` (up)) to `_input`
- **menu_widget.py**: add ability to change selection using `PageUp` and `PageDown`
- **main.py**: modify `test()` to now use `MenuWidget` instead of `DebugWidget`
- **menu_widget.py**: add a `MenuWidget` class.
- **container.py**: add a `loop` method
- **container.py**: add `move_relative` method
- **container.py**: add `move` method with centering functionality
- **container.py**: modify name of `draw_widget` to `refresh_all`
- **widget.py**: add `WidgetLoopEnd` Exception class
- **widget.py**: add `_wrap_str_to_width` method
- **window.py**: add `mvwin` method
- **window.py**: add `erase` method
- **window.py**: add call to `update_size` in `refresh`
- **window.py**: add `update_size` method
- **window.py**: add `self.beg_y` and `self.beg_x` variables
- **window.py**: add call to `self.keypad(True)` in `_common_init()`
- **map_layout.py**: add call to `main.test()`(the example container) from the `GameMap`
- **container.py**: add centering of the container relative to `content_win`
- **main.py**: move example container to its own function
- **main.py**: add a 'container' button for debugging purposes
- **debug_widget.py**: add a `DebugWidget` for debugging of `Container` and `Widget` classes
- **widget.py**: add `Widget` class
- **container.py**: add `Container` class
- **window.py**: modify title alignment (center > left)
- **window.py**: add `set_title()` method

### Fix

- **container.py**: fix error when calling `move` method of `Container` class
- **menu_widget.py**: fix TypeError when `None` provided as `info` argument in `MenuEntry`
- **menu_widget.py**: fix TypeError when `None` provided as `description`
- **container.py**: fix visual glitch when moving the container
- **menu_widget.py**: fix selection bugging out when `self.items` is smaller than `self.MENU_SIZE`
- **window.py**: fix wrong `beg_y` and `beg_x` being set when `update_size()` called
- **container.py**: fix info details appearing only for 0.1 seconds while `GameMap` loaded
- **main.py**: fix typo in import in `test()`
- fix double init of curses
- **window.py**: fix error when `set_title()` calls `window.refresh()` if it's a pad
- **window.py**: fix error when using `addstr()` with `-1` as `y` or `x`

### Refactor

- **main.py**: modify `main_menu` to use `Container` and `MenuWidget` instead of old `Menu` class

## 0.4.0 (2023-09-06)

### Feat

- **game_map.py**: add camera controls
- **game_map.py**: modify `GameMap()` class to use cell classes
- add cell classes
- **game_map.py**: replace `INTERACTIONS` with `self.interactions` in `_interact()` to avoid possible conflict
- **map_layout.py**: add some doors to the map for showcase
- **map_layout.py**: add functionality to `example_action()`
- **game_map.py**: modify behavior of interacting with interactions to be more intuitive
- **init.py**: change floor color to be more realistic
- **init.py**: add colors for door characters
- **game_map.py**: add door character `"d"` and `"D"` which use `Door()` class
- **door.py**: add `Door()` class
- **map_layout.py**: add floor to building
- **game_map.py**: modify texture of floor to add knots and cracks
- **game_map.py**: modify `self.grass_chars` for more realism
- **game_map.py**: add coordinates to `topbar.details_win`
- **init.py**: modify color of `GRASS_PAIR`
- **game_map.py**: modify not specified cells to be grass in _map_init()
- **game_map.py**: improve grass rendering
- **game_map.py**: utilize color; add floor, grass char
- **init.py**: add color support
- **game_map.py**: modify _move_player() to restore the original character before moving the player
- **game_map.py**: change _draw_map() to set attribute of interactive chars to cs.A_REVERSE
- **game_map.py**: change interaction behavior
- **loop.py**: add game_map._refresh_map() call
- **loop.py**: add terminal resize handling
- **game_map.py**: add _resize method
- **loop.py**: handle keypresses directly from loop and use new arguments in call to game_map._input()
- **game_map.py**: add _refresh_map() method for future use
- **game_map.py**: make _input() accept key presses as argument to work with game_loop()
- **game_map.py**: limit camera to not exceed positive map limit
- **main.py**: modify main_menu() to call game map
- **init.py**: add init_game_map()
- **loop.py**: add game loop
- **map_layout.py**: add map layout
- **game_map.py**: add open world
- **pad.py**: add curses pad support
- **window.py**: add *args and **kwargs for future pad management
- **window.py**: remove refresh() calls from border() and addstr() for more classic behavior

### Fix

- **init.py**: fix AttributeError when calling content_win.panel
- **game_map.py**: fix player moving when camera move called
- **game_map.py**: fix door glitching when interacted while door's position = player's position
- **door.py**: fix `__repr__()` not returning a string
- **game_map.py**: fix pad restricting map by being too small
- **game_map.py**: fix typo in calculation of `self.max_displayed_pad_size` in `_resize()` method
- **game_map.py**: adjust `pad_view_left` and `pad_view_top` calculations
- **game_map.py**: fix title not being displayed properly on topbar
- **game_map.py**: fix pad not spanning whole terminal
- **game_map.py**: fix player leaving behind a black box when moving first time
- **game_map.py**: fix player not appearing when map loaded
- **game_map.py**: fix error when going out of negative bounds
- **game_map.py**: fix screen flicker when moving
- **menu.py**: fix menu disappearing when content_win.panel's window replaced

### Refactor

- refactor curses initialization
- **game_map.py**: change variable name
- **game_map.py**: remove unnecessary additions in self.pad_size

## 0.3.0 (2023-07-31)

### Feat

- **board.py**: limit max movement speed
- **init.py**: make content_win not a panel
- **window.py**: update calls to SubWindow and DerWindow to include named args
- **window.py**: make make_panel and reverse named arguments
- **derwindow.py**: make make_panel and reverse named arguments
- **subwindow.py**: make make_panel and reverse named arguments
- **subwindow.py**: move addstr() and cs_addstr() to window.py
- **error_handler.py**: make full_path cleaner
- **main.py**: use error_handler on main_menu()
- **error_handler.py**: make exception menu description more concise
- **error_handler.py**: add retry option for caught exceptions
- **derwindow.py**: add DerWindow class
- **subwindow.py**: use _common_init() inherited from Window()
- **window.py**: add _common_init() to remove duplicate code

### Fix

- **menu.py**: fix borders not appearing
- **error_handler.py**: fix retrying not working correctly

### Refactor

- **menu.py**: implement window management on info_window and info_window_border
- **menu.py**: make description_window_border and description_window DerWindows
- **menu.py**: make root_window and root_window_border Windows instead of SubWindows
- **menu.py**: remove unused code
- **menu.py**: use f-string padding for label formatting

## 0.2.0 (2023-06-22)

### BREAKING CHANGE

- BREAKING CHANGE: remove obsolete functions
- move core folder to subfolder

### Feat

- **board.py**: add error_handler decorators
- **main.py**: add error_handler decorator back
- **.cz.toml**: remove gpg_sign
- **bump_version.yml**: comment out gpg key import
- **board.py**: implement window management
- **window.py**: add insch() method
- **menu.py**: implement window management
- **subwindow.py**: add cs_addstr method
- **init.py**: implement window management
- **window.py**: add curses methods to Window via encapsulation
- **window.py**: add curses.panel support
- **subwindow.py**: add curses.panel support
- **board.py**: update topbar call to match new implementation
- **main.py**: update topbar call to match new implementation
- **window.py**: add support for curses atrributes in whole window
- **topbar.py**: implement window management
- **subwindow.py**: add right alignment of text
- add window management
- **board.py**: add curses.beep when interacted with a collider
- **board.py**: add support for displaying board title on topbar

### Fix

- **bump_version.yml**: use new token
- **bump_version.yml**: add permission bypass to omit branch protection
- **bump_version.yml**: change token back to default
- **bump_version.yml**: fix permission denied when creating tag
- **bump_version.yml**: omit error when signing tag
- **subwindow.py**: fix error when using addstr() in a nested subwindow
- **subwindow.py**: fix error when nesting subwindows
- **window.py**: variable name typo

### Refactor

- **.cz.toml**: remove commented code
- **window.py**: remove unnecesarry blank lines
- **window.py**: fix whitespace in function definitions
- **topbar.py**: remove obsolete clear* and update* functions
- move simulat/core/windows to simulat/core/ui/windows

## 0.1.0 (2023-04-15)

### Feat

- **example.py**: add Board() examples
- **main.py**: add label to 'board' item in main menu
- **main.py**: change 'board' target to display example board
- **board.py**: add title rendering
- **menu.py**: add support for both args and kwargs in one target
- **board.py**: add support for doors
- **board.py**: extend door characters
- **__init__.py**: add __init__.py
- **main.py**: add board item to main menu for debigging purposes
- **board.py**: add support for custom board actions
- **board.py**: add board manager

### Fix

- **board.py**: fix error when only one of 'args' and 'kwargs' provided
- **menu.py**: fix error when only one of 'args', 'kwargs' provided
- **menu.py**: fix button padding
- **menu.py**: fix error when centered = True
- **board.py**: fix arrow keys not working
- **board.py**: fix '@' character visible in corner

### Refactor

- **board.py**: remove unnecesarry import and unused variable
- remove debug function
- **board.py**: change variable name board_str -> board_layout

## 0.1.0-dev.2 (2023-03-31)

### Feat

- **main.py**: remove debug code
- **menu.py**: correct info window position
- **menu.py**: correct button spacing and remove unnecessary code
- **menu.py**: update menu layout and info window width calculation to center properly
- add 'raise an  exception' button
- **core**: add error handler
- **ui**: add support for newlines in menu handler
- **ui**: clear menu windows upon cleanup
- **ui**: widened menu from 40 to 50 characters
- add exit option in main menu
- **ui**: add ability to describe buttons in menu handler
- **view**: add menu support for main menu
- **ui**: add menu handler

### Refactor

- remove need for using keys when not needed in menu handler

## 0.1.0-dev.1 (2023-03-17)

### Feat

- add main.py
- **init**: add init.py
- **ui**: add topbar

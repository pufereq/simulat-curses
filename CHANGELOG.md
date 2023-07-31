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

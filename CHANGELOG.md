## Unreleased

### BREAKING CHANGE

- move core folder to subfolder

### Feat

- **board.py**: add curses.beep when interacted with a collider
- **board.py**: add support for displaying board title on topbar

### Refactor

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

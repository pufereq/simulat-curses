#!/usr/bin/env python3

import sys
from curses import wrapper

from simulat.core.init import init_curses
from simulat.core.menu import Menu
from simulat.core.decorators.error_handler import error_handler


def main():
    init_curses()

    from simulat.core.init import content_win

    wrapper(main_menu, content_win)


# @error_handler
def main_menu(stdscr, content_win):
    from simulat.core.ui.windows.topbar import topbar

    topbar.update_title("main menu")
    menu = Menu(
        'main menu',
        'welcome to simulat!',
        [
            {
                'name': "new_game",
                'label': "new game",
                'info': "create a new game (not implemented yet)",
                'target': None
            },
            {
                'name': "exit",
                'info': "the most useful button",
                'target': sys.exit
            },
            {
                'name': "board",
                'label': "DEBUG: Example Board",
                'target': None
            }
        ],
        content_win
    )
    menu.display()

    if menu.result == 'new_game':
        raise NotImplementedError('not implemented (yet!)')
    elif menu.result == 'board':
        from simulat.core.ui.board.example import init_exampleboard
        init_exampleboard(content_win)
        # pass


if __name__ == '__main__':
    main()

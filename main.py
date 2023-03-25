#!/usr/bin/env python3

from curses import wrapper

from simulat.core.init import init_curses
from simulat.core.menu import Menu


def main():
    init_curses()

    from simulat.core.init import content_win

    wrapper(main_menu, content_win)


def main_menu(stdscr, content_win):
    from simulat.core.windows.topbar import topbar

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
        ],
        content_win
    )
    menu.display()

    if menu.result == 'new_game':
        raise NotImplementedError('not implemented (yet!)')


if __name__ == '__main__':
    main()

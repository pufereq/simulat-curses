#!/usr/bin/env python3

import sys
from curses import wrapper

from simulat.core.menu import Menu
from simulat.core.decorators.error_handler import error_handler


def main(stdscr):
    from simulat.core.init import init_curses_inner
    init_curses_inner(stdscr)

    main_menu(None)


@error_handler
def main_menu(stdscr):
    from simulat.core.ui.windows.topbar import topbar
    from simulat.core.init import content_win

    topbar.title_win.addstr(0, -1, "main menu")
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
            },
            {
                'name': "container",
                'label': "DEBUG: Example Container",
                'target': None
            },
        ],
        content_win
    )
    menu.display()

    if menu.result == 'new_game':
        raise NotImplementedError('not implemented (yet!)')
    elif menu.result == 'container':
        from simulat.core.ui.windows.window_management.container import Container
        from simulat.core.ui.windows.widgets.debug_widget import DebugWidget

        container = Container('lorem', 10, 10, 10, 10)
        container.widget = DebugWidget(container)

        while True:
            key = container.getch()

            if key == ord('d'):

                container.save()

                container.window.erase()
                container.refresh()

                container.window.mvwin(container.window.getbegyx()[0] + 1, container.window.getbegyx()[1] + 1)
                container.rewrite()
                container.draw_widget()
            elif key == ord('q'):
                break

    elif menu.result == 'board':
        from simulat.core.init import init_game_map
        init_game_map()


if __name__ == '__main__':
    wrapper(main)

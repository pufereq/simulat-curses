#!/usr/bin/env python3

import sys
import curses as cs

from simulat.core.menu import Menu
from simulat.core.ui.windows.window_management.container import Container
from simulat.core.ui.windows.widgets.menu_widget import MenuWidget, MenuEntry
from simulat.core.decorators.error_handler import error_handler


def main(stdscr):
    from simulat.core.init import init_curses_inner
    init_curses_inner(stdscr)

    main_menu(None)


@error_handler
def main_menu(stdscr):
    from simulat.core.ui.windows.topbar import topbar

    topbar.title_win.addstr(0, -1, "main menu")

    menu = Container('main menu', 'welcome to simulat!', 12, 36, "center", "center")
    menu.widget = MenuWidget(menu,
                             [
                                 MenuEntry("new_game", "new game", "create a new game (not implemented yet)", None),
                                 MenuEntry("exit", "exit", "the most useful button", sys.exit),
                                 MenuEntry("board", "DEBUG: Example Board", None, None),
                                 MenuEntry("container", "DEBUG: Example Container", None, None),
                             ]
                             )

    result = menu.loop()

    if result == 'new_game':
        raise NotImplementedError('not implemented (yet!)')
    elif result == 'container':
        test()

    elif result == 'board':
        from simulat.core.init import init_game_map
        init_game_map()


def test():
    from simulat.core.ui.windows.window_management.container import Container
    from simulat.core.ui.windows.widgets.menu_widget import MenuWidget, MenuEntry

    container = Container('lorem', 'ipsum dolor sit amet', 12, 30, "center", "center")
    container.widget = MenuWidget(container,
                                  [
                                      MenuEntry(f"test{i}", f"test{i}", f"test{i}\n{str(i)*10}", None) for i in range(100)
                                  ])
    result = container.loop()

    # raise Exception(result)
    container.widget.erase()
    container.widget.addstr(0, 0, f"selected: {result}\n\npress any key to exit")
    container.widget.refresh()
    container.getch()


if __name__ == '__main__':
    cs.wrapper(main)

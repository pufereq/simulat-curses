#!/usr/bin/env python3

from curses import wrapper

from simulat.core.init import init_curses


def main():
    init_curses()

    from simulat.core.init import content_win

    wrapper(main_menu, content_win)


def main_menu(stdscr, content_win):
    from simulat.core.windows.topbar import topbar

    topbar.update_title("main menu")
    topbar.top_bar.getch()


if __name__ == '__main__':
    main()

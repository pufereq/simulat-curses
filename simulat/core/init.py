#!/usr/bin/env python3

import curses as cs

from simulat.core.ui.windows.topbar import init_topbar
from simulat.core.ui.windows.window_management.window import Window


def init_stdscr(_scr):
    global stdscr, stdscr_height, stdscr_width

    stdscr = _scr
    stdscr_height, stdscr_width = stdscr.getmaxyx()

    cs.noecho()
    cs.cbreak()
    cs.curs_set(0)
    cs.start_color()


def init_content_win():
    global content_win, content_win_height, content_win_width

    content_win = Window(stdscr_height - 1, stdscr_width, 1, 0, make_panel=True)
    content_win_height, content_win_width = content_win.getmaxyx()


def init_curses():
    cs.wrapper(init_curses_inner)


def init_curses_inner(stdscr):
    from main import main_menu

    global content_win
    init_stdscr(stdscr)
    init_content_win()
    init_topbar(stdscr)

    main_menu(stdscr, content_win)

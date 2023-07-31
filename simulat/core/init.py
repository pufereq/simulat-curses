#!/usr/bin/env python3

import curses as cs

from simulat.core.ui.windows.topbar import init_topbar
from simulat.core.ui.windows.window_management.window import Window


def init_stdscr():
    global stdscr, stdscr_height, stdscr_width

    stdscr = cs.initscr()
    stdscr_height, stdscr_width = stdscr.getmaxyx()

    cs.noecho()
    cs.cbreak()
    cs.curs_set(0)
    cs.start_color()

    return stdscr


def init_content_win():
    global content_win, content_win_height, content_win_width

    content_win = Window(stdscr_height - 1, stdscr_width, 1, 0, make_panel=False)
    content_win_height, content_win_width = content_win.getmaxyx()


def init_curses():
    stdscr = init_stdscr()
    init_content_win()
    init_topbar(stdscr)

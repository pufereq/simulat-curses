#!/usr/bin/env python3


def init_simulat(stdscr):
    from .init_colors import init_colors
    from .init_ui import (init_stdscr, init_wrapper_win, init_content_win,
                          init_topbar, init_console)

    init_stdscr(stdscr)
    init_wrapper_win(34, 100)
    init_colors()
    init_content_win()
    init_console()
    init_topbar()

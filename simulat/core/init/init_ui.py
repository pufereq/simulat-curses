#!/usr/bin/env python3

import curses as cs

from simulat.core.ui.windows.window_management.window import Window


def init_stdscr(_scr):
    global stdscr, stdscr_height, stdscr_width

    stdscr = _scr
    stdscr_height, stdscr_width = stdscr.getmaxyx()

    cs.noecho()
    cs.cbreak()
    cs.curs_set(0)


def init_wrapper_win(size_y: int, size_x: int):
    global wrapper_win, wrapper_win_height, wrapper_win_width

    wrapper_win = Window(size_y, size_x, 0, 0, make_panel=False)
    wrapper_win_height, wrapper_win_width = wrapper_win.getmaxyx()


def init_content_win():
    global content_win, content_win_height, content_win_width

    content_win = Window(stdscr_height - 1, stdscr_width, 1, 0, make_panel=True)
    content_win_height, content_win_width = content_win.getmaxyx()

def init_topbar(debug_text: str = "simulat"):
    from .init_ui import wrapper_win
    from simulat.core.ui.windows.topbar import TopBar
    global topbar

    topbar = TopBar(wrapper_win, debug_text=debug_text)


def init_game_map():
    global topbar, game_map
    # Map
    from simulat.core.ui.game_map.game_map import GameMap

    game_map = GameMap()
    game_map._start_loop()


def init_console():
    global console
    # Console
    from simulat.core.ui.windows.console import Console

    console = Console("console", None, 16, 64, "center", "center")

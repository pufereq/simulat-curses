#!/usr/bin/env python3

import curses as cs
import time

from simulat.core.init import game_map, topbar


def game_loop():
    """The main loop handler.

    NOTE: This function is only the handler of the main loop. The actual
    loop is in `_loop()`.
    """
    from simulat.core.init import stdscr, wrapper_win, wrapper_win_height, wrapper_win_width

    FPS: int = 20  # frames per second
    FRAME_TIME: float = 1 / FPS

    stdscr.timeout(int(FRAME_TIME * 1000))

    last_frame_time = time.time()

    while True:
        current_time = time.time()
        keypress = stdscr.getch()

        required_size = wrapper_win_height, wrapper_win_width
        while stdscr.getmaxyx()[0] < required_size[0] or stdscr.getmaxyx()[1] < required_size[1]:
            wrapper_win.erase()
            wrapper_win.addstr(1, 0, "Please resize the terminal to a bigger size.")
            wrapper_win.addstr(2, 0, f"Current height: {stdscr.getmaxyx()[0]} (minimum: {required_size[0]})")
            wrapper_win.addstr(3, 0, f"Current width: {stdscr.getmaxyx()[1]} (minimum: {required_size[1]})")
            wrapper_win.refresh()
            wrapper_win.getch()

        if keypress == cs.KEY_RESIZE:
            cs.update_lines_cols()
            wrapper_win.resize(*required_size)
            topbar.fix_size()
            topbar.draw_all()
            game_map._resize()

        if current_time - last_frame_time >= FRAME_TIME:
            _loop(keypress)

            last_frame_time = current_time
        pass


def _loop(keypress: int):
    """The main loop.

    Args:
        keypress (int): The keypress to handle.
    """
    if keypress == ord("`"):
        from .init import console
        console.loop()


    game_map._input(keypress)
    game_map._refresh_map()

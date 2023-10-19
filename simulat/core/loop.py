#!/usr/bin/env python3

import curses as cs
import time

from simulat.core.init import game_map


def game_loop():
    """The main loop handler.

    NOTE: This function is only the handler of the main loop. The actual
    loop is in `_loop()`.
    """
    from simulat.core.init import stdscr

    FPS: int = 20  # frames per second
    FRAME_TIME: float = 1 / FPS

    stdscr.timeout(int(FRAME_TIME * 1000))

    last_frame_time = time.time()

    while True:
        current_time = time.time()
        keypress = stdscr.getch()

        if keypress == cs.KEY_RESIZE:
            cs.update_lines_cols()
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
    game_map._input(keypress)
    game_map._refresh_map()

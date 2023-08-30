#!/usr/bin/env python3

import curses as cs

def game_loop():
    from simulat.core.init import game_map
    from simulat.core.init import stdscr

    cs.halfdelay(1)

    while True:
        # get keypress
        keypress = stdscr.getch()

        if keypress == cs.KEY_RESIZE:
            cs.update_lines_cols()
            game_map._resize()

        game_map._input(keypress)

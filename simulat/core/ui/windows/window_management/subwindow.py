#!/usr/bin/env python3

"""Subwindow module."""

import curses as cs
import curses.panel

from .window import Window


class SubWindow(Window):
    def __init__(self, parent_window,
                 nlines: int, ncols: int,
                 y: int, x: int, *, make_panel: bool = False, reverse: bool = False):
        self.window = parent_window.subwin(nlines, ncols, y, x)
        self.max_y, self.max_x = self.window.getmaxyx()

        super()._common_init(reverse, make_panel)

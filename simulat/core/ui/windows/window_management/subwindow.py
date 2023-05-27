#!/usr/bin/env python3

"""Subwindow module."""

import curses as cs

from .window import Window


class SubWindow(Window):
    def __init__(self, parent_window,
                 nlines: int, ncols: int,
                 y: int, x: int, reverse: bool):
        self.window = parent_window.subwin(nlines, ncols, y, x)
        self.max_y, self.max_x = self.window.getmaxyx()

        if reverse:
            self.window.bkgd(' ', cs.A_REVERSE)
            self.window.attrset(cs.A_REVERSE)

    def addstr(self, y: int, x: int, _str: str, attr: int = cs.A_NORMAL):
        """
        Add a string to self.window.

        Args:
            y (int): Vertical location.
            x (int): Horizontal location.
            _str (str): String to add.
            atrr (int): Curses addstr string attribute.
            Defaults to cs.A_NORMAL.

        Location details:
            For _str to be centered on:
                x axis (horizontal), set x to -1.
                y axis (vertical), set y to -1.
            For curses to decide location (behavior when
                curses's addstr() function is supplied
                with only str (ad attr)), set x AND y to -2.
        """

        if y == -1:
            y = self.max_y // 2

        if x == -1:
            x = (self.max_x - len(_str)) // 2

        if x == -2 and y == -2:
            self.window.addstr(_str, attr)
        else:
            self.window.addstr(y, x, _str, attr)


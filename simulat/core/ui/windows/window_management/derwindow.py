#!/usr/bin/env python3

import curses as cs

from .subwindow import SubWindow


class DerWindow(SubWindow):
    def __init__(self, parent_window, nlines: int, ncols: int, rel_y: int, rel_x: int, *, make_panel: bool = False, reverse: bool = False):

        self.window = parent_window.derwin(nlines, ncols, rel_y, rel_x)

        super()._common_init(reverse, make_panel)

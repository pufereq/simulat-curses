#!/usr/bin/env python3

import curses as cs

from .window import Window


class Pad(Window):
    def __init__(self, nlines: int, ncols: int, *, reverse: bool = False, make_panel: bool = False):
        self.window = cs.newpad(nlines, ncols)
        super()._common_init(reverse, make_panel)

    def refresh(self, pminrow: int, pmincol: int, sminrow: int, smincol: int, smaxrow: int, smaxcol: int):
        self.window.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)

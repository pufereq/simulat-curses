#!/usr/bin/env python3

import curses as cs
import curses.panel


class Window():
    def __init__(self, nlines: int, ncols: int, y: int, x: int, reverse: bool = False, make_panel: bool = True, attrs: tuple | int = cs.A_NORMAL):
        self.window = cs.newwin(nlines, ncols, y, x)

        if type(attrs) is tuple:
            for attr in attrs:
                self.window.attrset(attr)
        else:
            self.window.attrset(attrs)

        self._common_init(reverse, make_panel)

    def _common_init(self, reverse: bool, make_panel: bool):
        if reverse:
            self.window.bkgd(' ', cs.A_REVERSE)
            self.window.attrset(cs.A_REVERSE)

        if make_panel:
            from .subwindow import SubWindow
            if type(self.window) is SubWindow:
                self.panel = curses.panel.new_panel(self.window.window)
            else:
                self.panel = curses.panel.new_panel(self.window)


    def clear(self):
        self.window.clear()

    def refresh(self):
        self.window.refresh()

    def border(self,
               ls=0, rs=0,
               ts=0, bs=0,
               tl=0, tr=0,
               bl=0, br=0):
        self.window.border(ls, rs, ts, bs, tl, tr, bl, br)
        self.refresh()

    def subwin(self, nlines: int, ncols: int, y: int, x: int, reverse: bool = False):
        from .subwindow import SubWindow
        return SubWindow(self.window, nlines, ncols, y, x, reverse)

    def derwin(self, nlines: int, ncols: int, y: int, x: int, reverse: bool = False):
        from .derwindow import DerWindow
        return DerWindow(self.window, nlines, ncols, y, x, reverse)

    def getch(self, *args):
        return self.window.getch(*args)

    def insch(self, ch, attr: int = cs.A_NORMAL):
        self.window.insch(ch, attr)

    def keypad(self, yes: bool):
        self.window.keypad(yes)

    def getmaxyx(self):
        return self.window.getmaxyx()

    def attron(self, attr: int):
        self.window.attron(attr)

    def attroff(self, attr: int):
        self.window.attroff(attr)

    def resize(self, nlines: int, ncols: int):
        self.window.resize(nlines, ncols)

    def move(self, y: int, x: int):
        self.panel.move(y, x)

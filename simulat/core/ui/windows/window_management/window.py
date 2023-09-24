#!/usr/bin/env python3

import curses as cs
import curses.panel


class Window():
    def __init__(self, nlines: int, ncols: int, y: int, x: int, *, make_panel: bool, reverse: bool = False, attrs: tuple | int = cs.A_NORMAL):
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

        self.keypad(True)

        self.beg_y, self.beg_x = self.window.getbegyx()
        self.max_y, self.max_x = self.window.getmaxyx()

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
            For _str to be aligned right, set x to -3.

        """
        from .subwindow import SubWindow

        if y == -1:
            y = self.max_y // 2

        if x == -1:
            x = (self.max_x - len(_str)) // 2

        if x == -3:
            x = self.window.getmaxyx()[1] - len(_str) - 1

        # add string
        if x == -2 and y == -2:
            if type(self.window) != SubWindow:
                self.window.addstr(_str, attr)
            else:
                self.window.cs_addstr(_str, attr)
        else:
            self.window.addstr(y, x, _str, attr)

    def update_size(self):
        self.max_y, self.max_x = self.window.getmaxyx()
        self.beg_x, self.beg_y = self.window.getbegyx()

    def cs_addstr(self, *args):
        self.window.addstr(*args)

    def clear(self):
        self.window.clear()

    def erase(self):
        self.window.erase()

    def refresh(self, *args, **kwargs):
        self.update_size()
        self.window.refresh(*args, **kwargs)

    def border(self,
               ls=0, rs=0,
               ts=0, bs=0,
               tl=0, tr=0,
               bl=0, br=0):
        self.window.border(ls, rs, ts, bs, tl, tr, bl, br)

    def set_title(self, title: str):
        self.addstr(0, 1, title)

    def subwin(self, nlines: int, ncols: int, y: int, x: int, *, make_panel: bool = False, reverse: bool = False):
        from .subwindow import SubWindow
        return SubWindow(self.window, nlines, ncols, y, x, make_panel=make_panel, reverse=reverse)

    def derwin(self, nlines: int, ncols: int, rel_y: int, rel_x: int, *, make_panel: bool = False, reverse: bool = False):
        from .derwindow import DerWindow
        return DerWindow(self.window, nlines, ncols, rel_y, rel_x, make_panel=make_panel, reverse=reverse)

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

    def mvwin(self, y: int, x: int):
        self.window.mvwin(y, x)

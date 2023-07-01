#!/usr/bin/env python3

from .window_management.window import Window

import curses as cs


class SideBar():
    def __init__(self) -> None:
        from simulat.core.init import stdscr_height, stdscr_width
        # define constants
        self.HEIGHT = stdscr_height - 1
        self.WIDTH = 60
        self.USABLE_HEIGHT = self.HEIGHT - 2
        self.USABLE_WIDTH = self.WIDTH - 1
        self.START_Y = 1
        self.START_X = stdscr_width - self.WIDTH
        self.usable_start_y = self.START_Y
        self.usable_start_x = self.START_X + 1

        # create sidebar window
        self.sidebar = Window(self.HEIGHT, self.WIDTH, self.START_Y, self.START_X)
        self.sidebar.attron(cs.A_REVERSE)
        try:
            self.sidebar.window.addstr(" \n" * self.HEIGHT)
        except cs.error:
            pass
        self.sidebar.attroff(cs.A_REVERSE)
        self.sidebar.refresh()

        # create subwindows
        # name window
        self.name_win_border = self.create_subwin(3, -1)
        self.name_win = self.name_win_border.innerwin()
        self.name_win_border.set_title('name')

        # money window
        self.money_win_border = self.create_subwin(4, -1)
        self.money_win = self.money_win_border.innerwin()
        self.money_win_border.set_title('budget')

        # TEST TODO: DELETE BELOW
        self.name_win.addstr(0, 0, "John Doe")
        # self.money_win.addstr(0, 0, "cash: $81.96\nbank: $16384.00")
        self.money_win.addstr(0, 0, "cash:\nbank:")
        self.money_win.addstr(0, 6, "$81.96", cs.A_BOLD)
        self.money_win.addstr(1, 6, "$4253.67", cs.A_BOLD)

    def _add_start_y(self, lines_added: int):
        self.usable_start_y += lines_added

    def create_subwin(self, height: int, width: int = -1, second_half_window: bool = False):
        if width == -1:
            width = self.USABLE_WIDTH
        elif width == -2:
            width = self.USABLE_WIDTH // 2

        if second_half_window:
            start_x = self.usable_start_x + width + 1
        else:
            start_x = self.usable_start_x

        newwin = self.sidebar.subwin(height, width, self.usable_start_y, start_x)

        if width == self.USABLE_WIDTH:
            self._add_start_y(newwin.getmaxyx()[0])

        newwin.border()
        newwin.refresh()

        return newwin


def init_sidebar():
    global sidebar

    sidebar = SideBar()

#!/usr/bin/env python3

import curses as cs

from simulat.core.decorators.error_handler import error_handler
from .window_management.derwindow import DerWindow


class TopBar():
    """
    Top Bar class. Used to inform user of basic game state (debug text,
    title of current screen, details). Layout as follows:
    /----------------------------------------------------------------\
    |debug text                   title                      details |
    |----------------------------------------------------------------|
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
    |                                                                |
   ...                                                              ...
    debug text - used to display debug statuses. Defaults to 'simulat'
    on __init__.
    title - set to current screen (action) name e.g. panel.
    details - displays game time. (TODO)
    """
    @error_handler
    def __init__(self, stdscr, debug_text: str = 'simulat'):
        """Initialize top bar.
        Args:
            stdscr (_CursesWindow): Standard (main) screen.
            debug_text (str): Debug text. Defaults to 'simulat'.
        """
        from simulat.core.init import wrapper_win
        global top_bar

        stdscr_height, stdscr_width = stdscr.getmaxyx()

        # create top bar
        self.top_bar = wrapper_win.derwin(1, wrapper_win.max_x, 0, 0, reverse=True)
        self.top_bar_height, self.top_bar_width = self.top_bar.getmaxyx()

        # create debug subwindow
        self.debug_win = self.top_bar.subwin(0, 20, 0, 0)
        self.debug_win_height, self.debug_win_width = self.debug_win.getmaxyx()

        # create title subwindow
        self.title_win = self.top_bar.subwin(0, self.top_bar_width - 40, 0, 20)
        self.title_height, self.title_width = self.title_win.getmaxyx()

        # create details subwindow
        self.details_win = self.top_bar.subwin(0, 20, 0, self.top_bar_width - 20)
        self.details_height, self.details_width = self.details_win.getmaxyx()

        # add debug text
        self.debug_win.addstr(-2, -2, debug_text)

        # DEBUG: add details text
        self.details_win.addstr(0, -3, 'TEST1234#')

        # DEBUG: add title
        self.title_win.addstr(0, -1, 'TEST1234#')

        # top_bar.addstr(str(len(main_character.first_name)))
        # details = ("time: soon")
        # self.top_bar.addstr(0, stdscr_width - len(details) - 1, details)
        stdscr.refresh()
        self.debug_win.refresh()
        self.title_win.refresh()
        self.details_win.refresh()
        self.top_bar.refresh()


@error_handler
def init_topbar(stdscr, debug_text: str = 'simulat'):
    global topbar

    topbar = TopBar(stdscr, debug_text)

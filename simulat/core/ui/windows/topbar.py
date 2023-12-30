#!/usr/bin/env python3

from simulat.core.decorators.error_handler import error_handler
from .window_management.derwindow import DerWindow


class TopBar(DerWindow):
    def __init__(self, parent, *, debug_text: str = "simulat"):
        """A bar with basic information about the game.

        Args:
            parent: Parent window of the topbar.
            debug_text (str): Debug text. Defaults to "simulat".

        Layout:
            /----------------------------------------------------------------\
            |debug text                   title                      details |
            +----------------------------------------------------------------+
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
            debug text: Field for displaying debug statuses. Can custom-set via the argument.
            title: The title of the contents.
            details: Miscellaneous information.
        """
        super().__init__(parent.window, 1, parent.getmaxyx()[1], 0, 0, make_panel=False, reverse=True)

        self.parent = parent

        self.debug_text: str = debug_text
        self.title_text: str = "test"
        self.details_text: str = "test"

        # calculate subwindows size
        proportion: tuple = (3, 4, 3)
        self.subwin_sizes: list = []
        for seg in proportion:
            self.subwin_sizes.append(int((self.max_x * seg) / sum(proportion)))

        # init subwindows
        self.debug_win = self.derwin(1, self.subwin_sizes[0], 0, 0)
        self.title_win = self.derwin(1, self.subwin_sizes[1], 0, self.subwin_sizes[0])
        self.details_win = self.derwin(1, self.subwin_sizes[2], 0, (self.subwin_sizes[0] + self.subwin_sizes[1]))

        self.window.bkgd("#")

        self.update_debug(self.debug_text)

        self.draw_debug()
        self.draw_title()
        self.draw_details()

        self.refresh_all()

    def refresh_all(self):
        self.refresh()
        self.debug_win.refresh()
        self.title_win.refresh()
        self.details_win.refresh()

    def fix_size(self):
        self.resize(1, self.parent.getmaxyx()[1])
        self.debug_win.resize(1, self.subwin_sizes[0])
        self.title_win.resize(1, self.subwin_sizes[1])
        self.details_win.resize(1, self.subwin_sizes[2])
        self.refresh_all()

    def draw_debug(self):
        self.debug_win.erase()
        self.debug_win.addstr(0, 1, self.debug_text)
        self.debug_win.refresh()

    def draw_title(self):
        self.title_win.erase()
        self.title_win.addstr(0, -1, self.title_text)
        self.title_win.refresh()

    def draw_details(self):
        self.details_win.erase()
        self.details_win.addstr(0, -3, self.details_text)
        self.details_win.refresh()

    def draw_all(self):
        self.draw_debug()
        self.draw_title()
        self.draw_details()

    def update_debug(self, text: str):
        self.debug_text = text
        self.draw_debug()

    def update_title(self, text: str):
        self.title_text = text
        self.draw_title()

    def update_details(self, text: str):
        self.details_text = text
        self.draw_details()


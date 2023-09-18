#!/usr/bin/env python3

from ..window_management.derwindow import DerWindow


class Widget(DerWindow):
    def __init__(self, parent):
        super().__init__(parent.window, parent.max_y - 2, parent.max_x - 2, 1, 1, make_panel=False)

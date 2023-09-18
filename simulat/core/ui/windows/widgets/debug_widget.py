#!/usr/bin/env python3

from .widget import Widget


class DebugWidget(Widget):
    def __init__(self, parent):
        super().__init__(parent)
        try:
            self.addstr(0, 0, "lorem ipsum dolor sit amet " * 3)
        except Exception:
            pass
        self.refresh()

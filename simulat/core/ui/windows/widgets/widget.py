#!/usr/bin/env python3

from ..window_management.derwindow import DerWindow


class WidgetLoopEnd(Exception):
    """Raised when a widget ends the parent Container's loop.

    Is supposed to be caught by the container.
    """
    pass


class Widget(DerWindow):
    def __init__(self, parent):
        super().__init__(parent.window, parent.max_y - 4, parent.max_x - 2, 3, 1, make_panel=False)

        self.result = None

    def _wrap_str_to_width(self, text: str):
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            for i in range(0, len(line), self.max_x - 2):
                new_lines.append(line[i:i + self.max_x - 2])
        return '\n'.join(new_lines)

    def _input(self, key: int):
        pass  # for static widgets

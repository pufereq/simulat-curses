#!/usr/bin/env python3

from ..window_management.derwindow import DerWindow


class Widget(DerWindow):
    def __init__(self, parent):
        super().__init__(parent.window, parent.max_y - 2, parent.max_x - 2, 1, 1, make_panel=False)

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

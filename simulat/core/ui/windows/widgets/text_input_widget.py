#!/usr/bin/env python3

import curses as cs
from curses.textpad import Textbox

from .widget import Widget, WidgetLoopEnd
from ..window_management.derwindow import DerWindow


class TextInputWidget(Widget):
    def __init__(self, parent, *, default_text: str = ""):
        super().__init__(parent)

        self.default_text = default_text

        # init input window
        self.input_window = DerWindow(self.window, self.max_y - 2,
                                      self.max_x - 2, 0, 1, make_panel=False)
        self.is_one_line = self.input_window.max_y == 1

        self.textbox = Textbox(self.input_window.window, insert_mode=True)

        # add tip text
        self.addstr(self.max_y - 1, 1,
                    "press `Return` to submit" if self.is_one_line
                    else "press `Ctrl-G` to submit", cs.A_DIM)

        # refresh
        self.refresh()
        self.input_window.refresh()

        # set cursor
        cs.curs_set(2)  # show cursor

    def _input(self, key):
        if key in [cs.KEY_ENTER, 10] and self.is_one_line or key == 7:
            cs.curs_set(0)  # hide cursor
            raise WidgetLoopEnd(self.textbox.gather().strip("\n").strip(' '))
        else:
            self.textbox.do_command(key)
            self.input_window.refresh()

    def mvwin(self, y: int, x: int):
        self.input_window.mvwin(y, x + 1)
        return super().mvwin(y, x)


def test_textinputwidget():
    from ..window_management.container import Container

    container1 = Container("text input widget test", "lorem ipsum, one line",
                           7, 28,
                           "center", "center")
    container1.widget = TextInputWidget(container1)
    result1 = container1.loop()

    container2 = Container("text input widget test", "lorem ipsum, multiline",
                           8, 28,
                           "center", "center")
    container2.widget = TextInputWidget(container2)
    result2 = container2.loop()

    raise Exception(result1, result2)

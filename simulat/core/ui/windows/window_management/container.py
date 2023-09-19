#!/usr/bin/env python3

from .window import Window

from simulat.core.init import content_win


class Container(Window):
    def __init__(self, title: str, nlines: int, ncols: int, y: int | str, x: int | str):

        if y == "center":
            y = (content_win.max_y - nlines) // 2
        if x == "center":
            x = (content_win.max_x - ncols) // 2

        super().__init__(nlines, ncols, y, x, make_panel=True)

        self.title = title
        self.widget = None

        self.update_title(self.title)

    def update_title(self, title: str):
        self.title = title
        self.border()
        self.set_title(title)
        self.refresh()

    def draw_widget(self):
        self.widget.refresh()
        self.refresh()

    def save(self):
        self.window_contents = [[self.window.inch(y, x) for x in range(self.max_x)] for y in range(self.max_y)]
        return self.window_contents

    def rewrite(self):
        self.window.erase()
        for y, line in enumerate(self.window_contents):
            for x, char in enumerate(line):
                self.window.insch(y, x, char)
        self.refresh()

    # def attach(self, window: Widget

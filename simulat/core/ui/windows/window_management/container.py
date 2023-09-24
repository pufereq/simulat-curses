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

    def refresh_all(self):
        self.widget.refresh()
        self.refresh()

    def save(self):
        self.window_contents = [[self.window.inch(y, x)
                                for x in range(self.max_x)]
                                for y in range(self.max_y)]
        return self.window_contents

    def rewrite(self):
        self.window.erase()
        for y, line in enumerate(self.window_contents):
            for x, char in enumerate(line):
                self.window.insch(y, x, char)
        self.refresh()

    def move(self, new_y: int | str, new_x: int | str):
        if new_y == "center":
            new_y = (content_win.getmaxyx()[0] - self.max_y) // 2
        if new_x == "center":
            new_x = (content_win.getmaxyx()[1] - self.max_x) // 2

        self.beg_x, self.beg_y = new_x, new_y

        self.save()
        self.erase()
        self.refresh_all()

        self.mvwin(new_y, new_x)
        self.widget.mvwin(new_y + 1, new_x + 1)

        self.rewrite()

        self.refresh_all()

    def move_relative(self, rel_y: int, rel_x: int):
        self.move(self.beg_y + rel_y, self.beg_x + rel_x)

    # def attach(self, window: Widget

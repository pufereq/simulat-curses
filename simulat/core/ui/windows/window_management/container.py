#!/usr/bin/env python3

import curses as cs

from .window import Window

from ..widgets.widget import WidgetLoopEnd



class Container(Window):
    def __init__(self, title: str, description: str | None, nlines: int, ncols: int, y: int | str, x: int | str):
        from simulat.core.init import content_win

        if y == "center":
            y = (content_win.max_y - nlines) // 2
        if x == "center":
            x = (content_win.max_x - ncols) // 2

        super().__init__(nlines, ncols, y, x, make_panel=True)

        self.title = title
        self.description = description if description else "No description provided."
        self.widget = None

        self.update_title(self.title)
        self.update_description(self.description)

    def loop(self):
        cs.cbreak()

        while True:
            key = self.getch()

            try:
                self.widget._input(key)
            except WidgetLoopEnd:
                break

            if key == ord('d'):
                self.move_relative(1, 1)
            elif key == cs.KEY_RESIZE:
                self.move("center", "center")
            elif key == ord('q'):
                break

        cs.halfdelay(1)
        return self.widget.result

    def update_title(self, title: str):
        self.title = title
        self.border()
        self.set_title(title)
        self.refresh()

    def update_description(self, description: str):
        self.description = description
        self.addstr(1, 1, f"{description:^{self.max_x - 2}}", cs.A_ITALIC)
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
        self.widget.mvwin(new_y + 3, new_x + 1)

        self.rewrite()

        self.refresh_all()

    def move_relative(self, rel_y: int, rel_x: int):
        self.move(self.beg_y + rel_y, self.beg_x + rel_x)

    # def attach(self, window: Widget

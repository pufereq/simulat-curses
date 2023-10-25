#!/usr/bin/env python3

import curses as cs

from .window import Window

from ..widgets.widget import WidgetLoopEnd


class Container(Window):
    """A container window that can hold other windows (widgets)."""
    def __init__(self, title: str, description: str | None, nlines: int, ncols: int, y: int | str, x: int | str):
        """A container window that can hold other windows (widgets).

        Args:
            title (str): The title of the window.
            description (str | None): The description of the window.
            nlines (int): The number of lines of the window (height).
            ncols (int): The number of columns of the window (width).
            y (int | str): The y position of the window. Accepts "center".
            x (int | str): The x position of the window. Accepts "center".
        """
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
        """Starts the loop of the container window.

        Returns:
            Any: The result of the widget's loop.
        """

        result = None  # default

        while True:
            key = self.getch()

            if key == -1:
                continue

            try:
                self.widget._input(key)
            except WidgetLoopEnd as e:
                result = e.args[0]
                break

            if key == ord('d'):
                self.move_relative(1, 1)
            elif key == cs.KEY_RESIZE:
                self.move("center", "center")
            elif key == ord('q'):
                break

        return result

    def update_title(self, title: str):
        """Updates the title of the window.

        Args:
            title (str): The new title.
        """
        self.title = title
        self.border()
        self.set_title(title)
        self.refresh()

    def update_description(self, description: str):
        """Updates the description of the window.

        Args:
            description (str): The new description.
        """
        self.description = description
        self.addstr(1, 1, f"{description:^{self.max_x - 2}}", cs.A_ITALIC)
        self.refresh()

    def refresh_all(self):
        """Refreshes the window and the widget."""
        self.widget.refresh()
        self.refresh()

    def save(self):
        """Saves the contents (all chars) of the window."""
        self.window_contents = [[self.window.inch(y, x)
                                for x in range(self.max_x)]
                                for y in range(self.max_y)]
        return self.window_contents

    def rewrite(self):
        """Rewrites the contents of the window."""
        self.window.erase()
        for y, line in enumerate(self.window_contents):
            for x, char in enumerate(line):
                self.window.insch(y, x, char)
        self.refresh()

    def move(self, new_y: int | str, new_x: int | str):
        """Moves the window to a new position.

        Args:
            new_y (int | str): The new y position of the window. Accepts "center".
            new_x (int | str): The new x position of the window. Accepts "center".
        """
        from simulat.core.init import content_win
        if new_y == "center":
            new_y = (content_win.getmaxyx()[0] - self.max_y) // 2
        if new_x == "center":
            new_x = (content_win.getmaxyx()[1] - self.max_x) // 2

        self.beg_x, self.beg_y = new_x, new_y

        # prepare for moving
        self.save()
        self.erase()
        self.refresh_all()

        # move
        self.mvwin(new_y, new_x)
        self.widget.mvwin(new_y + 3, new_x + 1)

        # rewrite contents
        self.rewrite()
        self.refresh_all()

    def move_relative(self, rel_y: int, rel_x: int):
        """Moves the window relative to its current position.

        Args:
            rel_y (int): The relative y position of the window.
            rel_x (int): The relative x position of the window.
        """
        self.move(self.beg_y + rel_y, self.beg_x + rel_x)

    # def attach(self, window: Widget


def container_test():
    from simulat.core.ui.windows.window_management.container import Container
    from simulat.core.ui.windows.widgets.menu_widget import MenuWidget, MenuEntry

    container = Container('lorem', 'ipsum dolor sit amet', 12, 30, "center", "center")
    container.widget = MenuWidget(container,
                                  [
                                      MenuEntry(f"test{i}", f"test{i}", f"test{i}\n{str(i)*10}", None) for i in range(100)
                                  ])
    result = container.loop()

    # raise Exception(result)
    container.widget.erase()
    container.widget.addstr(0, 0, f"selected: {result}\n\npress any key to exit")
    container.widget.refresh()
    container.getch()

#!/usr/bin/env python3

import curses as cs

from .widget import Widget, WidgetLoopEnd


class MenuEntry():
    """A menu entry for the MenuWidget.

    Args:
        name (str): The name of the entry.
        label (str): The label of the entry.
        info (str | None): The info of the entry.
        target (callable, optional): The target of the entry. Defaults to None.
        locked (bool, optional): Whether the entry is locked. Defaults to False.
    """
    def __init__(self, name: str, label: str, info: str | None,
                 target: callable = None, /, locked: bool = False):
        """A menu entry for the MenuWidget.

        Args:
            name (str): The name of the entry.
            label (str): The label of the entry.
            info (str | None): The info of the entry.
            target (callable, optional): The target of the entry. Defaults to None.
            locked (bool, optional): Whether the entry is locked. Defaults to False.
        """
        self.name = name
        self.label = label
        self.info = info if info else "No info provided."
        self.target = target
        self.locked = locked

    def __repr__(self):
        return f"<MenuEntry name={self.name} label={self.label} info={self.info} target={self.target}>"


class MenuWidget(Widget):
    """A menu widget.

    Args:
        parent (Container): The parent container window.
        items (list[MenuEntry,]): The menu entries.
    """
    def __init__(self, parent, items: list[MenuEntry,]):
        """A menu widget.

        Args:
            parent (Container): The parent container window.
            items (list[MenuEntry,]): The menu entries.
        """
        super().__init__(parent)

        self.items = items
        self.selected = 0
        self.selected_entry = self.items[self.selected]

        self.MENU_SIZE = self.max_y - 3

        self.display()
        self.refresh()

    def display(self):
        """Displays the widget."""
        self.erase()
        self.refresh()

        start_index = min(max(self.selected - (self.MENU_SIZE // 2), 0),
                          len(self.items) - self.MENU_SIZE
                          if len(self.items) > self.MENU_SIZE else 0)
        end_index = min(start_index + self.MENU_SIZE, len(self.items))
        displayed_items = self.items[start_index:end_index]

        self.MENU_OFFSET = self.MENU_SIZE // 2 - len(displayed_items) // 2

        for i, item in enumerate(displayed_items):
            text = f"<{item.label:^{self.max_x - 4}}>"
            if item.locked:
                attr = cs.A_DIM
            else:
                attr = cs.A_NORMAL

            if i == self.selected - start_index:
                self.addstr(i + self.MENU_OFFSET, 1, text, cs.A_REVERSE | attr)
            else:
                self.addstr(i + self.MENU_OFFSET, 1, text, attr)

        info_text = ("locked: " if self.selected_entry.locked else "") + self.selected_entry.info
        info_text = self._wrap_str_to_width(info_text).split("\n")[0]

        if len(info_text.split("\n")[0]) > self.max_x - 4:
            info_text = info_text[:-1] + "…"

        self.addstr(self.max_y - 2, 1, info_text, cs.A_DIM)
        self.addstr(self.max_y - 1, 1, "press `i` for more info", cs.A_DIM | cs.A_ITALIC)

    def _display_info(self):
        """Displays the info of the selected entry."""
        info_text = self.selected_entry.info
        info_text = self._wrap_str_to_width(info_text)
        info_text_split = info_text.strip().split("\n")

        self.erase()

        self.addstr(0, 1, f"{self.selected_entry.label:^{self.max_x - 2}}", cs.A_BOLD)

        for idx, line in enumerate(info_text_split):
            info_text_formatted = line, cs.A_DIM

            self.addstr(idx + 1, 1, *info_text_formatted)

        self.addstr(self.max_y - 1, 1, "press any key to return", cs.A_DIM | cs.A_ITALIC)

        self.getch()
        self.refresh()

    def _input(self, key: int):
        """Handles the input of the widget.

        Args:
            key (int): The key that was pressed.

        Raises:
            WidgetLoopEnd: Raised when the widget ends the parent Container's loop.

        Keybinds:
            `up` or `k`: Select the previous entry.
            `down` or `j`: Select the next entry.
            `page up`: Select the previous entry by half the menu size.
            `page down`: Select the next entry by half the menu size.
            `enter`: Select the current entry.
            `i`: Display the info of the current entry.
        """
        if key in [cs.KEY_UP, ord('k')]:
            self.selected = max(self.selected - 1, -1)
            if self.selected == -1:
                self.selected = len(self.items) - 1

            self.selected_entry = self.items[self.selected]

        elif key in [cs.KEY_DOWN, ord('j')]:
            self.selected = min(self.selected + 1, len(self.items) - 0)
            if self.selected == len(self.items):
                self.selected = 0

            self.selected_entry = self.items[self.selected]

        elif key == cs.KEY_NPAGE:
            self.selected = min(self.selected + (self.MENU_SIZE // 2), len(self.items) - 0)
            if self.selected == len(self.items):
                self.selected = 0

            self.selected_entry = self.items[self.selected]

        elif key == cs.KEY_PPAGE:
            self.selected = max(self.selected - (self.MENU_SIZE // 2), -1)
            if self.selected == -1:
                self.selected = len(self.items) - 1

            self.selected_entry = self.items[self.selected]

        elif key == ord('i'):
            self._display_info()

        elif key == cs.KEY_ENTER or key == ord('\n'):
            # cancel if locked
            if self.items[self.selected].locked:
                return

            if self.items[self.selected].target is not None:
                self.items[self.selected].target()
                raise WidgetLoopEnd(None)
            else:
                self.result = self.items[self.selected].name
                raise WidgetLoopEnd(self.items[self.selected].name)

        self.display()
        self.refresh()

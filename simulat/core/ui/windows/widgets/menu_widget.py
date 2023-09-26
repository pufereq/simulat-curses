#!/usr/bin/env python3

import curses as cs

from .widget import Widget, WidgetLoopEnd


class MenuEntry():
    def __init__(self, name: str, label: str, info: str, target: callable = None, /, locked: bool = False):
        self.name = name
        self.label = label
        self.info = info
        self.target = target
        self.locked = locked

    def __repr__(self):
        return f"<MenuEntry name={self.name} label={self.label} info={self.info} target={self.target}>"


class MenuWidget(Widget):
    def __init__(self, parent, items: list[MenuEntry,]):
        super().__init__(parent)

        self.items = items
        self.selected = 0
        self.selected_entry = self.items[self.selected]

        self.MENU_SIZE = 5

        self.display()
        self.refresh()

    def display(self):
        self.erase()
        self.refresh()

        start_index = min(max(self.selected - (self.MENU_SIZE // 2), 0),
                          len(self.items) - self.MENU_SIZE
                          if len(self.items) > self.MENU_SIZE else 0)
        end_index = min(start_index + self.MENU_SIZE, len(self.items))
        displayed_items = self.items[start_index:end_index]

        for i, item in enumerate(displayed_items):
            text = f"<{item.label:^{self.max_x - 4}}>"
            if item.locked:
                attr = cs.A_DIM
            else:
                attr = cs.A_NORMAL

            if i == self.selected - start_index:
                self.addstr(i, 1, text, cs.A_REVERSE | attr)
            else:
                self.addstr(i, 1, text, attr)

        info_text = self.selected_entry.info
        info_text = self._wrap_str_to_width(info_text).split("\n")[0]

        if len(info_text.split("\n")[0]) > self.max_x - 4:
            info_text = info_text[:-1] + "…"

        self.addstr(self.max_y - 2, 1, info_text, cs.A_DIM)
        self.addstr(self.max_y - 1, 1, "press `i` for more info", cs.A_DIM | cs.A_ITALIC)

    def _display_info(self):
        info_text = self.selected_entry.info
        info_text = self._wrap_str_to_width(info_text)
        info_text_split = info_text.strip().split("\n")

        self.erase()

        self.addstr(0, 1, f"{'info: ' + self.selected_entry.label:^{self.max_x - 2}}", cs.A_BOLD)

        for idx, line in enumerate(info_text_split):
            info_text_formatted = line, cs.A_DIM

            self.addstr(idx + 2, 1, *info_text_formatted)

        self.getch()
        self.refresh()

    def _input(self, key: int):
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
            if self.items[self.selected].target is not None:
                self.items[self.selected].target()
                raise WidgetLoopEnd(None)
            else:
                self.result = self.items[self.selected].name
                raise WidgetLoopEnd(self.items[self.selected].name)

        self.display()
        self.refresh()

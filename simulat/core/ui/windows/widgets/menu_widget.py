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

        start_index = min(max(self.selected - (self.MENU_SIZE // 2), 0), len(self.items) - self.MENU_SIZE)
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
        info_text = self._wrap_str_to_width(info_text)
        info_text_split = info_text.strip().split("\n")

        info_text_y_pos = len(info_text_split)

        for line in info_text_split:
            info_text_formatted = line, cs.A_DIM

            self.addstr(self.max_y - info_text_y_pos, 1, *info_text_formatted)

            info_text_y_pos -= 1

    def _input(self, key: int):
        if key == cs.KEY_UP:
            self.selected = max(self.selected - 1, -1)
            if self.selected == -1:
                self.selected = len(self.items) - 1

            self.selected_entry = self.items[self.selected]

        elif key == cs.KEY_DOWN:
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

        elif key == cs.KEY_ENTER or key == ord('\n'):
            if self.items[self.selected].target is not None:
                self.items[self.selected].target()
                raise WidgetLoopEnd(None)
            else:
                self.result = self.items[self.selected].name
                raise WidgetLoopEnd(self.items[self.selected].name)

        self.display()
        self.refresh()

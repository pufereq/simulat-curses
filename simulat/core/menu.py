#!/usr/bin/env python3
"""Curses menu handler."""

import math
import itertools
import curses as cs
from curses import panel

LINE_HEAVY = "┃"


class Menu():
    """Menu generation using curses."""

    def __init__(self, title: str, description: str,
                 items: list[dict], window, centered: bool = True) -> None:
        """Initialize Menu class.

        Args:
            title (str): Menu title.
            description (str): Menu description.
            items (list[dict]): Menu items. See below for examples.
            window (Any): Window to display menu in.
            centered (bool): Center menu position. Defaults to True.

        Examples:
            items=[
                {
                    'label': "(str) Label of the button".
                    'target': "(func | None) Target function".
                    Leave none if checked manually using menu.result().
                    'args': "(list) Function arguments. Leave empty if none."
                    'kwargs': "(dict) Function keyword arguments. Leave empty if none."
                },
                {
                    'label': "foo",
                    'target': bar,
                    'args': {'name': "John Doe"}
                },
                ...
            ]
        """
        # initialize panels

        added_height: int = 0
        for line in description.split('\n'):
            added_height += math.ceil(len(line) / 50) if line != '' else 1
        self.added_description_height: int = added_height + 2

        self.root_vertical_length: int = len(items) + self.added_description_height - 1
        self.vertical_length: int = len(items)
        self.size = window.getmaxyx()

        self.parent_window = window
        self.parent_window_horizontal_length = self.parent_window.getmaxyx()[1]

        self.description: str = description

        # iterate through menu entries (items) and set `label` to `name` if
        # no `label` was specified.
        for _dict in items:
            if "label" not in _dict:
                _dict['label'] = _dict['name']

        # create `labels` list and populate it with `label` variables
        # from each item.
        labels: list = list((_dict['label'] for _dict in items))

        # add `title` of menu to `labels`, then set max horizontal length
        # of all labels. cheesy af.
        # labels.append(title)
        strings: list = labels.copy()
        strings.append(title)
        strings.append(description)

        for idx, _str in enumerate(strings):
            strings[idx] = _str.split('\n')

        strings = list(itertools.chain.from_iterable(strings))
        self.horizontal_length: int = len(max(strings, key=len))

        if self.horizontal_length >= 50:
            self.horizontal_length = 50

        self.horizontal_length += 2 if len(self.description) > len(max(labels, key=len)) else 6

        # labels.remove(title)
        root_height: int = (self.size[0] // 2) - self.root_vertical_length if centered else self.size[0] - self.root_vertical_length - self.added_description_height - 4
        root_width: int = (self.size[1] - self.horizontal_length) // 2

        self.info_height: int = root_height + self.root_vertical_length + 5

        # create windows
        # try:
        self.root_window_border = window.subwin(
            self.root_vertical_length + 4,
            self.horizontal_length,
            root_height,
            root_width
        )
        self.root_window = window.subwin(
            self.root_vertical_length + 4,
            self.horizontal_length,
            root_height,
            root_width
        )

        self.menu_window = self.root_window.subwin(
            self.vertical_length + 1,
            self.horizontal_length - 2,
            root_height + 1 + self.added_description_height,
            root_width + 1
        )

        self.description_window_border = self.root_window_border.subwin(
            self.added_description_height,
            self.horizontal_length,
            root_height if self.added_description_height > 2 else root_height + 1,
            root_width
        )

        self.description_window = self.root_window.subwin(
            self.added_description_height - 2,
            self.horizontal_length - 2,
            root_height + 1,
            root_width + 1
        )

        self.info_window_border = cs.newwin(
            3,
            1,
            self.info_height,
            root_width
        )

        self.info_window = cs.newwin(
            1,
            1,
            self.info_height + 1,
            root_width + 1
        )

        # except cs.error:
        #     raise Exception("Window too small!")
        self.root_window_border.border(0, 0, 1, 0, 0, 1, 0, 0)
        self.info_window.border()

        self.info_panel = panel.new_panel(self.info_window)
        self.info_panel_border = panel.new_panel(self.info_window_border)
        self.info_panel.hide()

        # add description window border
        separator = '┡' + '━' * (self.horizontal_length - 2) + '┩'

        try:
            for line in range(self.added_description_height - 1):
                self.description_window_border.addstr(line, 0, LINE_HEAVY)
                self.description_window_border.addstr(line, self.horizontal_length - 1, LINE_HEAVY)

            self.description_window_border.addstr(self.added_description_height - 1, 0, separator)
        except cs.error:
            pass  # this for some reason throws an exception, passing does not break anything

        # draw title bar
        self.root_window_border.attron(cs.A_REVERSE)
        self.root_window_border.addstr(0, 0, ' ' * self.horizontal_length, cs.A_REVERSE)
        self.root_window_border.attroff(cs.A_REVERSE)

        # add title on bar
        self.root_window_border.addstr(0, (self.root_window_border.getmaxyx()[1] - len(title)) // 2, title, cs.A_REVERSE)
        self.root_window.keypad(1)

        self.panel = panel.new_panel(self.root_window)
        self.panel.hide()

        # add description
        try:
            self.description_window.addstr(description)  # same as before; passing does not break anything
        except cs.error:
            pass

        panel.update_panels()

        self.pos: int = 0
        self.items: list = items

    def navigate(self, n):
        self.pos += n
        if self.pos < 0:
            self.pos = 0
        elif self.pos >= len(self.items):
            self.pos = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()

        while True:
            self.root_window.refresh()
            cs.doupdate()
            for idx, item in enumerate(self.items):
                if idx == self.pos:
                    mode = cs.A_REVERSE
                    if 'info' not in item:
                        item['info'] = ''
                    entry_info_str: str = item['info']

                    if entry_info_str != '':
                        info_str: list = []
                        for _str in entry_info_str.split('\n'):
                            info_str.append(_str)

                        info_len: int = len(max(info_str, key=len))

                        self.info_window_horizontal_length = info_len + 1 if info_len <= 50 else 50
                        self.info_width = (self.parent_window_horizontal_length - self.info_window_horizontal_length) // 2 - 1

                        added_height: int = 0
                        for line in entry_info_str.split('\n'):
                            added_height += math.ceil(len(line) / 50) if line != '' else 1
                        self.added_info_height = added_height

                        self.info_panel.move(self.info_height, self.info_width + 1)
                        self.info_panel_border.move(self.info_height - 1, self.info_width)

                        self.info_window.resize(self.added_info_height, self.info_window_horizontal_length)
                        self.info_window_border.resize(self.added_info_height + 2, self.info_window_horizontal_length + 2)

                        self.info_window.clear()
                        self.info_window_border.clear()
                        self.info_window_border.border()
                        self.info_window_border.refresh()

                        self.info_panel_border.replace(self.info_window_border)
                        self.info_panel.replace(self.info_window)

                        self.info_panel.top()

                        try:
                            self.info_window.addstr(entry_info_str)
                        except cs.error:
                            pass

                        self.info_window.refresh()

                    # self.info_window.refresh()
                    panel.update_panels()
                    cs.doupdate()

                else:
                    mode = cs.A_NORMAL

                label = item['label']
                label_len = len(label)

                window_size = self.menu_window.getmaxyx()

                if self.horizontal_length % 2 == 0:
                    if label_len % 2 == 0:
                        right_spacing: int = 0
                    else:
                        right_spacing: int = -1
                else:
                    if label_len % 2 == 0:
                        right_spacing: int = -1
                    else:
                        right_spacing: int = 0
                padding = 1

                text_pos = (window_size[1] - len(label)) // 2 - padding

                # this gibberish formats the label to be shown on the menu.
                label: str = ' ' * (text_pos) + label + ' ' * (text_pos - right_spacing)
                self.menu_window.addstr(0 + idx, padding, label, mode)
                self.menu_window.refresh()
                self.info_window.refresh()

            key = self.root_window.getch()

            # item chosen
            if key in [cs.KEY_ENTER, ord('\n')]:
                chosen_item = self.items[self.pos]
                self.result: str = chosen_item['name']

                # if chosen menu entry's target function is none, break.
                # user can later use `self.result` returned by self.results()
                if 'target' not in chosen_item or chosen_item['target'] is None:
                    break

                if 'args' not in chosen_item:
                    chosen_item['args'] = []
                if 'kwargs' not in chosen_item:
                    chosen_item['kwargs'] = {}

                chosen_item['target'](*chosen_item['args'], **chosen_item['kwargs'])

            # navigation
            elif key in (cs.KEY_UP, ord('k')):
                self.navigate(-1)
            elif key in (cs.KEY_DOWN, ord('j')):
                self.navigate(1)

            self.info_window.clear()
            self.info_window_border.clear()
            self.info_window.refresh()

        # cleanup
        self.root_window.clear()
        self.info_window.clear()
        self.info_window_border.clear()
        self.root_window.refresh()
        self.info_window.refresh()
        self.info_window_border.refresh()

        self.panel.hide()
        panel.update_panels()
        cs.doupdate()

    def results(self) -> str:
        return self.result

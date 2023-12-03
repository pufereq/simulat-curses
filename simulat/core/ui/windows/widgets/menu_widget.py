#!/usr/bin/env python3

import curses as cs

from .widget import Widget, WidgetLoopEnd


class MenuEntry():
    """A menu entry for the MenuWidget."""
    def __init__(self, name: str, label: str, info: str | None,
                 target: callable = None, /,
                 locked: bool = False, locked_msg: str | None = None):
        """A menu entry for the MenuWidget.

        Args:
            name (str): The name of the entry.
            label (str): The label of the entry.
            info (str | None): The info of the entry.
            target (callable, optional): The target of the entry. Defaults to None.
            locked (bool, optional): Whether the entry is locked. Defaults to False.
            locked_msg (str | None, optional): The message to display
            when the entry is locked. Defaults to None.
        """
        self.name = name
        self.label = label
        self.formatted_label = label
        self.info = info if info else "No info provided."
        self.target = target
        self.locked = locked
        self.locked_msg = locked_msg

    def __repr__(self):
        return f"<MenuEntry name={self.name} label={self.label} info={self.info} target={self.target}>"


class ToggleEntry(MenuEntry):
    """A toggle entry for the MenuWidget."""
    def __init__(self, name: str, label: str, info: str | None, *, default_value: bool, locked: bool = False, locked_msg: str | None = None):
        super().__init__(name, label, info, None, locked, locked_msg)

        self.value = default_value
        self.update_label()

    def update_label(self):
        """Updates the label of the entry."""
        self.formatted_label = f"{self.label} [{'x' if self.value else ' '}]"

    def toggle(self):
        """Toggles the value of the entry."""
        self.value = not self.value


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
            text = f"<{item.formatted_label:^{self.max_x - 4}}>"
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
        self.addstr(self.max_y - 1, 1, "press `?` for help", cs.A_DIM | cs.A_ITALIC)

    def _display_info(self):
        """Displays the info of the selected entry.

        Obsolete by `_display_notification()` but kept for reference.
        """
        self._display_notification(self.selected_entry.info)

    def _display_notification(self, text: str):
        """Displays a notification.

        Args:
            text (str): The text to display.
        """
        self.erase()

        self.addstr(0, 1, f"{self.selected_entry.label:^{self.max_x - 2}}", cs.A_BOLD)
        text = self._wrap_str_to_width(text)
        text_split = text.strip().split("\n")

        for idx, line in enumerate(text_split):
            text_formatted = line, cs.A_DIM

            self.addstr(idx + 1, 1, *text_formatted)

        self.addstr(self.max_y - 1, 1, "press any key to return", cs.A_DIM | cs.A_ITALIC)

        self.getch()
        self.display()
        self.refresh()

    def _show_locked_msg(self, entry: MenuEntry | ToggleEntry):
        """Checks if the selected entry is locked and displays a message if it is."""
        self._display_notification(f"this entry is locked. reason:\n{entry.locked_msg if entry.locked_msg else 'no reason provided'}")

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
        # one entry up
        if key in [cs.KEY_UP, ord('k')]:
            self.selected = max(self.selected - 1, -1)
            if self.selected == -1:
                self.selected = len(self.items) - 1

            self.selected_entry = self.items[self.selected]

        # one entry down
        elif key in [cs.KEY_DOWN, ord('j')]:
            self.selected = min(self.selected + 1, len(self.items) - 0)
            if self.selected == len(self.items):
                self.selected = 0

            self.selected_entry = self.items[self.selected]

        # half page up
        elif key == cs.KEY_NPAGE:
            self.selected = min(self.selected + (self.MENU_SIZE // 2), len(self.items) - 0)
            if self.selected == len(self.items):
                self.selected = 0

            self.selected_entry = self.items[self.selected]

        # half page down
        elif key == cs.KEY_PPAGE:
            self.selected = max(self.selected - (self.MENU_SIZE // 2), -1)
            if self.selected == -1:
                self.selected = len(self.items) - 1

            self.selected_entry = self.items[self.selected]

        # display info
        elif key == ord('i'):
            self._display_notification(self.selected_entry.info)

        # display help
        elif key == ord('?'):
            from ..window_management.container import Container

            help_text = {
                "Navigation": [
                    ["`UP`", "focus the previous entry"],
                    ["`DOWN`", "focus the next entry"],
                    ["`PAGE UP`", "scroll half screen up"],
                    ["`PAGE DOWN`", "scroll half screen down"],
                ],
                "Interaction": [
                    ["`ENTER`", "select the current entry"],
                    ["`SPACE`", "toggle the current entry"],
                    ["`i`", "display info of current entry"],
                ],
                "Miscellaneous": [
                    ["`q`", "return to the previous menu"],
                    ["`?`", "display this help message"],
                ],
            }

            MAX_WIDTH = 40

            # create container
            help_container = Container(None, None, 18, MAX_WIDTH, "center", "center")
            help_container.widget = Widget(help_container)

            # add help text
            line = 0
            for idx, (category, contents) in enumerate(help_text.items()):
                help_container.widget.addstr(line, -1, f"{category: ^{MAX_WIDTH - 10}}", cs.A_BOLD | cs.A_UNDERLINE)
                line += 1
                for _idx, help_line in enumerate(contents):
                    help_container.widget.addstr(line, 0, '.' * (MAX_WIDTH - 3), cs.A_DIM)
                    help_container.widget.addstr(line, 0, help_line[0], cs.A_BOLD)
                    help_container.widget.addstr(line, -3, help_line[1], cs.A_ITALIC)
                    line += 1
                line += 1

            # add tip text
            help_container.widget.addstr(help_container.widget.max_y - 1, -1, "press `q` to return", cs.A_DIM | cs.A_ITALIC)

            help_container.widget.refresh()
            help_container.loop()
            help_container.widget.erase()
            help_container.erase()
            help_container.refresh_all()

            return

        # toggle entry
        elif key in [ord(' '), cs.KEY_ENTER, ord('\n')]:
            # show locked message if locked
            if self.items[self.selected].locked:
                self._show_locked_msg(self.items[self.selected])
                return

            if key == ord(' '):
                if isinstance(self.items[self.selected], ToggleEntry):
                    self.items[self.selected].toggle()
                    self.items[self.selected].update_label()
                    self.display()
                    self.refresh()
                    return
                else:
                    self._display_notification("this entry is not toggleable. to select instead, press `ENTER`")

            elif key in [cs.KEY_ENTER, ord('\n')]:
                if isinstance(self.items[self.selected], ToggleEntry):
                    self._display_notification("this entry is not selectable. to toggle instead, press `SPACE`")
                else:  # prevent selecting toggle entries
                    if self.items[self.selected].target is not None:
                        self.items[self.selected].target()
                        raise WidgetLoopEnd(None)
                    else:
                        self.result = self.items[self.selected].name
                        raise WidgetLoopEnd(self.items[self.selected].name)

        self.display()
        self.refresh()

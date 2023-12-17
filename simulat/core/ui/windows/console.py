#!/usr/bin/env python3

import curses as cs
import curses.panel

from .window_management.container import Container
from .widgets.text_input_widget import TextInputWidget


class Console(Container):
    def __init__(self, title: str, description: str | None, nlines: int, ncols: int, y: int | str, x: int | str):
        super().__init__(title, description, nlines, ncols, y, x)

        self.widget = TextInputWidget(self, default_text="command")

    def loop(self):
        result = ("import simulat; " + (super().loop() or "")).replace("\n", "")
        try:
            parsed = compile(result, "<string>", "exec")
        except Exception as e:
            self.show_result(f"{e.__class__.__name__}: {e}")
            return

        self.show_result(self.execute_command(parsed))

    def show_result(self, result):
        from .window_management.container import Container
        from .widgets.widget import Widget

        self.panel.hide()
        self.widget.panel.hide()
        curses.panel.update_panels()

        container = Container("console result", str(result), 10, 40, "center", "center")
        container.widget = Widget(container)

        container.display()
        container.refresh_all()
        container.loop()

    def execute_command(self, command: str):
        """Executes a command.

        Args:
            command (str): The command to execute.
        """
        try:
            return eval(command)
        except Exception as e:
            self.show_result(f"{e.__class__.__name__}: {e}")

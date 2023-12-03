#!/usr/bin/env python3

from simulat.core.ui.windows.window_management.container import Container
from simulat.core.ui.windows.widgets.menu_widget import MenuWidget, MenuEntry, ToggleEntry
from simulat.core.ui.windows.widgets.text_input_widget import TextInputWidget


def menu_widget_test():
    container = Container('lorem', 'ipsum dolor sit amet', 16, 36, "center", "center")
    container.widget = MenuWidget(container,
            [
                MenuEntry("text_input", "DEBUG: Text Input Widget", None, None),
                MenuEntry("menu", "DEBUG: Menu Widget", None, None),
                MenuEntry("toggle", "DEBUG: Toggle Entry", None, None),
            ]
        )
    result = container.loop()

    if result == 'text_input':
        container.widget.erase()
        container.widget = TextInputWidget(container)
        result = container.loop()
    elif result == 'menu':
        container.widget = MenuWidget(container,
            [
                MenuEntry(f"test{i}", f"test{i}", f"test{i}", None) for i in range(100)
            ]
        )
        result = container.loop()
    elif result == 'toggle':
        container.widget = MenuWidget(container,
            [
                ToggleEntry(f"test{i}", f"test{i}", f"test{i}", default_value=i % 3, locked=i % 4) for i in range(10)
            ] + [
                MenuEntry("back", "back", "back", None)
            ]
        )
        result = container.loop()
        container.widget.erase()
        toggled = container.widget.get_toggle_entries()
        container.widget.addstr(0, 0, f"selected: {result}")
        container.widget.addstr(1, 0, str(toggled))
        container.widget.refresh()
        container.getch()
        menu_widget_test()

    # raise Exception(result)
    container.widget.erase()
    container.widget.addstr(0, 0, f"selected: {result}\n\npress any key to exit")
    container.widget.refresh()
    container.getch()

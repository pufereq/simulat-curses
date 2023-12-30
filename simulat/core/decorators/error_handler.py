#!/usr/bin/env python3

import curses as cs
import os
import functools
import inspect

from simulat.core.menu import Menu


def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global function, arguments
        function = func
        arguments = args, kwargs

        try:
            return func(*args, **kwargs)
        except Exception as exc:
            filepath = inspect.getsourcefile(func)
            full_path = os.path.relpath(filepath, '.')
            full_path = './' + full_path

            error_menu(full_path, func.__name__, exc)
    return wrapper


def error_menu(full_path: str, func_name: str, exc: Exception):
    from simulat.core.init.init_ui import content_win

    exc_name = type(exc).__name__

    # formatted_message = f"{full_path}:{func_name}:{exc_name} - {exc}"
    title = f"{exc_name}"
    # message = f"an exception occured in:\n{full_path}:{func_name}()\n\n{exc_name}: {exc}"
    message = f"""\
an exception occured in
{full_path}:{func_name}()
{exc_name}: {exc}\
"""

    menu = Menu(
        title,
        message,
        [
            {
                'name': "continue",
                'info': "(DANGEROUS) continue runtime anyway",
                'target': None
            },
            {
                'name': "retry",
                'info': "retry runtime",
                'target': None
            },
            {
                'name': "exit",
                'info': 'exit simulat',
                'target': None
            }
        ],
        content_win
    )

    menu.display()

    if menu.result == 'continue':
        submenu = Menu(
            "continue?",
            "are you sure to continue?\nit (probably) will break the game",
            [
                {
                    'name': "no",
                    'info': "go back to exception menu"
                },
                {
                    'name': 'yes',
                    'info': "continue runtime of game with errors.\nWILL DESTROY THE SAVE FILE"
                }
            ],
            content_win
        )
        # menu.root_window.clear()
        menu.root_window.refresh()
        submenu.display()

        if submenu.result == 'no':
            error_menu(full_path, func_name, exc)
        elif submenu.result == 'yes':
            pass

    elif menu.result == 'retry':
        _retry(function, *arguments[0], **arguments[1])
    elif menu.result == 'exit':
        cs.endwin()
        raise exc


@error_handler
def _retry(func, *args, **kwargs):
    func(*args, *kwargs)

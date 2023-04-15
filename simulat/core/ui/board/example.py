#!/usr/bin/env python3

from typing import Final

from .board import Board

"""
An example of using Board() with subclasses.

Contains two classes (boards).
"""


def init_exampleboard(window):
    board = ExampleBoard(window)
    board.display()


class ExampleBoard(Board):
    def __init__(self, window) -> None:
        TITLE: Final = "Example 1"
        LAYOUT: Final = """\
###############################
#                             #
#                             #
#                             #
#                             #
#                       a     #
#                             #
#                             A
#                             #
#                             #
#                             #
#       b                     #
#                             #
#                             #
#                             #
###############################\
"""
        INTERACTIONS: Final = {
            'actions': {
                'a': {
                    'title': "TEST",
                    'description': "lorem ipsum dolor sit amet",
                    'actions': [
                        {
                            'name': "foo",
                            'info': "execute foo",
                            'target': self.foo,
                            'args': [8],
                            'kwargs': {'arg2': 2}
                        }
                    ]
                },
                'b': {
                    'title': "TEST",
                    'description': "lorem ipsum dolor sit amet",
                    'actions': [
                        {
                            'name': "bar",
                            'info': "execute bar",
                            'target': self.bar,
                            'args': [2, 3, 5]
                        }
                    ]
                }
            },
            'doors': {
                'A': {
                    'goto': example2call,
                    'args': [window]
                }
            }
        }
        super().__init__(window, TITLE, LAYOUT, INTERACTIONS)
        # super().display()

    def foo(self, arg1: int, arg2: int):
        raise Exception(f'Foo executed! Result: {arg1 - arg2}')

    def bar(self, *args):
        raise Exception(f'Bar executed! Result: {sum(args)}')


def example2call(window):
    ex2 = Example2Board(window)
    ex2.display()


class Example2Board(Board):
    def __init__(self, window) -> None:
        TITLE: Final = "Example 2"
        LAYOUT: Final = """\
###############################
#                             #
#                             #
#     b                       #
#     b                       #
#     b                       #
#     b                       A
#                             A
#                             #
#                             #
#                             #
#                  aaaa       #
#                             #
#                             #
#                             #
###############################\
"""
        INTERACTIONS: Final = {
            'actions': {
                'a': {
                    'title': "TEST",
                    'description': "lorem ipsum dolor sit amet",
                    'actions': [
                        {
                            'name': "foo",
                            'info': "execute foo",
                            'target': self.foo,
                            'args': [8],
                            'kwargs': {'arg2': 2}
                        }
                    ]
                },
                'b': {
                    'title': "TEST",
                    'description': "lorem ipsum dolor sit amet",
                    'actions': [
                        {
                            'name': "bar",
                            'info': "execute bar",
                            'target': self.bar,
                            'args': [2, 3, 5]
                        }
                    ]
                }
            },
            'doors': {
                'A': {
                    'goto': init_exampleboard,
                    'args': [window]
                }
            }
        }
        super().__init__(window, TITLE, LAYOUT, INTERACTIONS)

    def foo(self, arg1: int, arg2: int):
        raise Exception(f'Foo executed! Result: {arg1 - arg2}')

    def bar(self, *args):
        raise Exception(f'Bar executed! Result: {sum(args)}')

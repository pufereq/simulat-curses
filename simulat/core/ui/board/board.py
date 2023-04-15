#!/usr/bin/env python3

import curses as cs
from curses import panel
# from simulat.core.init import content_win

from simulat.core.menu import Menu
from simulat.core.init import content_win


boardstr = """\
###############################
#        a                    #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#             b               #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
###############################\
"""


class Board():

    def __init__(self, window, board_layout: str) -> None:
        self.board_layout = board_layout
        self.materials = self.define_materials()
        self.define_actions('')
        board_size_y, board_size_x = 16, 32
        # WALL = ''
        # DOOR = ''
        PLAYER = '@'

        self.parent_window_y, self.parent_window_x = window.getmaxyx()

        self.root_window_location = (self.parent_window_y - board_size_y) // 2, (self.parent_window_x - board_size_x) // 2
        self.root_window = window.subwin(
            board_size_y + 2,
            board_size_x + 4,
            self.root_window_location[0] - 1,
            self.root_window_location[1] - 2
        )
        self.board_window = self.root_window.subwin(
            board_size_y,
            board_size_x,
            self.root_window_location[0],
            self.root_window_location[1]
        )
        self.player_window = cs.newwin(
            1,
            1,
            self.root_window_location[0] + 1,
            self.root_window_location[1] + 1
        )

        self.player_panel = panel.new_panel(self.player_window)
        self.board_panel = panel.new_panel(self.board_window)

        # draw player
        self.player_y, self.player_x = 7, 15
        self.set_abs_position()
        self.player_panel.move(self.abs_player_y, self.abs_player_x)
        self.player_window.refresh()
        self.player_window.insch(PLAYER)
        # self.player_window.clear()

        # prepare board
        # split board into nested lists of characters in lines
        self.board = []
        for line in board_layout.splitlines():
            line_list = []

            for char in line:
                line_list.append(char)

            self.board.append(line_list)

        # draw border around root_window
        self.root_window.border()
        self.root_window.refresh()

        # draw board
        for y, line in enumerate(self.board):
            for x, char in enumerate(line):
                # line = 'haga'
                self.board_window.addstr(y, x, char)
                self.board_window.refresh()

        # finishing up, fixes arrow keys not working
        self.player_window.keypad(True)

    def display(self):
        self.player_panel.top()
        while True:
            self.set_abs_position()
            # refresh and move player panel to new location
            cs.doupdate()
            self.player_panel.top()
            self.player_panel.move(self.abs_player_y, self.abs_player_x)
            self.board_window.refresh()
            self.player_window.refresh()
            panel.update_panels()

            # wait for input
            key = self.player_window.getch()

            if key in [cs.KEY_LEFT, ord('h'), ord('a')]:
                self.move(0, -1)
            elif key in [cs.KEY_UP, ord('k'), ord('w')]:
                self.move(-1, 0)
            elif key in [cs.KEY_DOWN, ord('j'), ord('s')]:
                self.move(1, 0)
            elif key in [cs.KEY_RIGHT, ord('l'), ord('d')]:
                self.move(0, 1)

    def define_materials(self):
        self.materials = {
            '#': 'wall',
            'X': 'door'
        }
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.materials[letter] = 'action'

        # get collision positions
        self.interactive_positions = {
            'colliding': [],
            'actions': [],
            'doors': []
        }

        for y, line in enumerate(self.board_layout.splitlines()):
            for x, char in enumerate(line):
                # if char == '\n' or char == ' ':
                if char not in self.materials:
                    pass
                elif self.materials[char] == 'wall':
                    self.interactive_positions['colliding'].append((y, x))
                elif self.materials[char] == 'action':
                    self.interactive_positions['actions'].append((y, x))
                elif self.materials[char] == 'door':
                    self.interactive_positions['doors'].append((y, x))
        print()

    def define_actions(self, actions: dict[dict]):
        self.actions = {
            'a': {
                'title': 'foo',
                'description': 'lorem ipsum',
                'actions': [
                    {
                        'name': 'use',
                        'label': 'use that shit!',
                        'info': 'lorem ipsum dolor sit amet',
                        'target': print()
                    }
                ]
            }
        }
        for idx, name in enumerate(self.actions):
            self.actions[name]['actions'].append(
                {
                    'name': 'back'
                }
            )





    def move(self, y: int, x: int):
        new_pos = (self.player_y + y, self.player_x + x)
        if new_pos in self.interactive_positions['colliding']:
            return
        elif new_pos in self.interactive_positions['actions']:
            action_id = self.board[new_pos[0]][new_pos[1]]
            action = self.actions[action_id]
            action_menu = Menu(
                action['title'],
                action['description'],
                action['actions'],
                content_win,
                False
            )
            action_menu.display()

        self.player_y += y
        self.player_x += x
        self.set_abs_position()

    def set_abs_position(self):
        self.abs_player_y = self.player_y + self.root_window_location[0]
        self.abs_player_x = self.player_x + self.root_window_location[1]

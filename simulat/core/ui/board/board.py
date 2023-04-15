#!/usr/bin/env python3

import curses as cs
from curses import panel

from simulat.core.menu import Menu


class Board():
    """
    Board object.

    Draws a board on which the user can interact with objects on it.
    """
    def __init__(self, window, title: str, board_layout: str, interactions: dict) -> None:
        """Initialize Board().

        Args:
            window (_CursesWindow): Window to display board in. The board
            is centered both horizontally and vertically. Also needs
            window size at least 20x36.
            board_layout (str): Board layout, details below. Defaults to boardstr.

        Board Layout (board_layout):
            A str containing the layout.
            Recommended approach is to use multiline strings.

            Board should be of size 16x32 (y, x). The player always spawns
            at (7, 15).

            Layout:
                Player interacts with objects assigned to characters.

                Characters:
                    Colliders:
                    #: wall, a collider. Player cannot move through it.

                    Interactive:
                    A-Z: door, upon making contact with it, executes
                    defined function without confirmation.
                    a-z: action, upon contact displays menu (Menu()) with specified
                    items.

                    Other:
                    @: the player.

                    NOTE: Characters not specified above are ignored and
                    without colission.

                Conventions:
                    Board MUST be enclosed in characters (walls, doors)
                    to prevent the player escaping the board.

                Example:
                    \"\"\"\
                    ###############################
                    #        a                    #
                    #                             #
                    #                             #
                    #                             #
                    #                             #
                    #                             #
                    #                             A
                    #             b               #
                    #                             #
                    #                             #
                    #                             #
                    #                             #
                    #                             #
                    #                             #
                    ###############################\
                    \"\"\"
        """
        self.board_layout = board_layout
        self.interactions = interactions
        self.materials = self.define_materials()
        self.title = title
        board_size_y, board_size_x = 16, 32
        PLAYER = '@'

        # add back button to every action's menu
        for idx, name in enumerate(self.interactions['actions']):
            self.interactions['actions'][name]['actions'].append(
                {
                    'name': 'back'
                }
            )

        self.parent_window_y, self.parent_window_x = window.getmaxyx()
        self.parent_window = window

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

        # draw board title
        _, root_window_width = self.root_window.getmaxyx()
        self.root_window.addstr(0, (root_window_width - len(self.title)) // 2, self.title)

        self.root_window.refresh()

        # draw board
        for y, line in enumerate(self.board):
            for x, char in enumerate(line):
                self.board_window.addstr(y, x, char)
                self.board_window.refresh()

        # finishing up, fixes arrow keys not working
        self.player_window.keypad(True)

    def display(self):
        """Display player and board."""
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
        }

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.materials[letter] = 'action'

        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.materials[letter] = 'door'

        # get collision positions
        self.interactive_positions = {
            'colliding': [],
            'actions': [],
            'doors': []
        }

        for y, line in enumerate(self.board_layout.splitlines()):
            for x, char in enumerate(line):
                if char not in self.materials:
                    pass
                elif self.materials[char] == 'wall':
                    self.interactive_positions['colliding'].append((y, x))
                elif self.materials[char] == 'action':
                    self.interactive_positions['actions'].append((y, x))
                elif self.materials[char] == 'door':
                    self.interactive_positions['doors'].append((y, x))

    def move(self, y: int, x: int):
        """Move the player character

        Args:
            y (int): relative y axis
            x (int): relative x axis

        Raises:
            KeyError: if no details for action specified

        Returns:
            NoneType: aborts if new position is a collider
        """
        new_pos = (self.player_y + y, self.player_x + x)
        if new_pos in self.interactive_positions['colliding']:
            return  # if new position is a collider, abort

        elif new_pos in self.interactive_positions['actions'] or \
                new_pos in self.interactive_positions['doors']:

            interaction_symbol = self.board[new_pos[0]][new_pos[1]]  # interaction_symbol is the letter representing the action (e.g. 'b')

            # define type of interaction (action, door)
            for _dict in self.interactions:
                if interaction_symbol in self.interactions[_dict]:
                    interaction_type = _dict
                    break
            else:
                raise KeyError(f"Interaction {interaction_symbol} not found in self.interactions (but on board)")

            interaction = self.interactions[interaction_type][interaction_symbol]

            if interaction_type == 'actions':
                action_menu = Menu(
                    interaction['title'],
                    interaction['description'],
                    interaction['actions'],
                    self.parent_window,
                    False
                )
                action_menu.display()

            elif interaction_type == 'doors':
                interaction = self.interactions['doors'][interaction_symbol]

                if 'args' not in interaction:
                    interaction['args'] = []
                if 'kwargs' not in interaction:
                    interaction['kwargs'] = {}

                interaction['goto'](*interaction['args'], **interaction['kwargs'])

        self.player_y += y
        self.player_x += x
        self.set_abs_position()

    def set_abs_position(self):
        """Set absolute position on screen."""
        self.abs_player_y = self.player_y + self.root_window_location[0]
        self.abs_player_x = self.player_x + self.root_window_location[1]

#!/usr/bin/env python3

import time
import curses as cs
from curses import panel

from simulat.core.menu import Menu
from simulat.core.ui.windows.topbar import topbar
from simulat.core.init import stdscr

from simulat.core.decorators.error_handler import error_handler

from simulat.core.ui.windows.window_management.window import Window
from simulat.core.ui.windows.window_management.subwindow import SubWindow


class Board():
    """
    Board object.

    Draws a board on which the user can interact with objects on it.
    """
    @error_handler
    def __init__(self, window, title: str, board_layout: str, interactions: dict) -> None:
        """Initialize Board().

        Args:
            window (_CursesWindow): Window to display board in. The board
            is centered both horizontally and vertically. Also needs
            window size at least 20x36.
            title (str): Board's title. Displayed in top-center of board border.
            board_layout (str): Board layout, details below. Defaults to boardstr.
            interactions (dict): Interaction dict. Example in ./example.py.

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
                    NOTE: There can be more than one same action IDs
                    used (letters). Example below.

                Conventions:
                    Board MUST be enclosed in characters (walls, doors)
                    to prevent the player escaping the board.

                Example:
                    See more detailed examples in ./example.py
                    \"\"\"
                    ###############################
                    #        a      a             #
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
        self.movement_delay = 0.3  # seconds
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
        self.root_window = SubWindow(
            self.parent_window,
            board_size_y + 2,
            board_size_x + 4,
            self.root_window_location[0] - 1,
            self.root_window_location[1] - 2
        )
        self.board_window = SubWindow(
            self.parent_window,
            board_size_y,
            board_size_x,
            self.root_window_location[0],
            self.root_window_location[1],
            make_panel=True
        )
        self.player_window = Window(
            1,
            1,
            self.root_window_location[0] + 1,
            self.root_window_location[1] + 1,
            make_panel=True,
        )

        self.player_panel = self.player_window.panel
        self.board_panel = self.board_window.panel

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

        # set title on topbar
        topbar.title_win.addstr(0, -1, f"board: {title}", cs.A_BOLD)

    def handle_input(self):
        key = stdscr.getch()
        if key != -1:
            current_time = time.time()

            if current_time - self.last_move_time >= self.movement_delay:
                if key in [cs.KEY_LEFT, ord('h'), ord('a')]:
                    self.move(0, -1)
                elif key in [cs.KEY_UP, ord('k'), ord('w')]:
                    self.move(-1, 0)
                elif key in [cs.KEY_DOWN, ord('j'), ord('s')]:
                    self.move(1, 0)
                elif key in [cs.KEY_RIGHT, ord('l'), ord('d')]:
                    self.move(0, 1)

                self.last_move_time = current_time

    @error_handler
    def display(self):
        """Display player and board."""
        self.player_panel.top()
        self.last_move_time = time.time()
        while True:
            self.set_abs_position()
            # refresh and move player panel to new location
            cs.doupdate()
            # self.player_panel.top()
            self.player_panel.move(self.abs_player_y, self.abs_player_x)
            self.board_window.refresh()
            self.player_window.refresh()
            panel.update_panels()

            self.handle_input()

    @error_handler
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

    @error_handler
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
        self.last_move_time = time.time()
        new_pos = (self.player_y + y, self.player_x + x)
        if new_pos in self.interactive_positions['colliding']:
            cs.beep()
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

    @error_handler
    def set_abs_position(self):
        """Set absolute position on screen."""
        self.abs_player_y = self.player_y + self.root_window_location[0]
        self.abs_player_x = self.player_x + self.root_window_location[1]

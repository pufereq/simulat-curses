#!/usr/bin/env python3

import curses as cs
from curses import panel
# from simulat.core.init import content_win


boardstr = """\
###############################
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
#                             #
###############################\
"""


class Board():
    def __init__(self, window, board_str: str = boardstr) -> None:
        BOARD_SIZE_Y, BOARD_SIZE_X = 16, 32
        # WALL = ''
        # DOOR = ''
        PLAYER = '@'


        self.parent_window_y, self.parent_window_x = window.getmaxyx()

        self.root_window_location = (self.parent_window_y - BOARD_SIZE_Y) // 2, (self.parent_window_x - BOARD_SIZE_X) // 2
        self.root_window = window.subwin(
            BOARD_SIZE_Y + 2,
            BOARD_SIZE_X + 4,
            self.root_window_location[0] - 1,
            self.root_window_location[1] - 2
        )
        self.board_window = self.root_window.subwin(
            BOARD_SIZE_Y,
            BOARD_SIZE_X,
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
        for line in board_str.splitlines():
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

        # get collision positions
        self.collision = []
        for y, line in enumerate(self.board):
            for x, char in enumerate(line):
                if char == '#':
                    self.collision.append((y, x))

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

    def move(self, y: int, x: int):
        new_pos = (self.player_y + y, self.player_x + x)
        if new_pos in self.collision:
            # pass
            return
        self.player_y += y
        self.player_x += x
        self.set_abs_position()

    def set_abs_position(self):
        self.abs_player_y = self.player_y + self.root_window_location[0]
        self.abs_player_x = self.player_x + self.root_window_location[1]

#!/usr/bin/env python3

import time
import curses as cs

from typing import Final

from simulat.core.ui.windows.topbar import topbar
from simulat.core.init import stdscr

from simulat.core.init import content_win

from simulat.core.ui.windows.window_management.pad import Pad

from ....data.map_layouts.map_layout import MAP_LAYOUT, INTERACTIONS, TITLE


class GameMap():
    def __init__(self):
        self.MAP_SIZE: Final = 100, 100
        self.pad_size = self.MAP_SIZE[0], self.MAP_SIZE[1]  # subject to change when user resizes terminal

        self.map_layout = self._map_init(MAP_LAYOUT)
        self.collision_matrix = self._collision_matrix_init(self.map_layout)
        self.interactions = INTERACTIONS
        self.title = TITLE
        self.movement_delay = 0.0  # seconds

        self.player_char = '@'
        self.player_pos = 1, 1

        self.max_size = stdscr.getmaxyx()[0] - 2, stdscr.getmaxyx()[1] - 1

        self.map = Pad(*self.pad_size)
        content_win.panel.replace(self.map.window)

        # set title
        topbar.title_win.addstr(0, -1, self.title)
        topbar.title_win.refresh()

        # init player
        # self.player_window = SubWindow(self.map, 1, 1, 0, 0, make_panel=True)
        self.player_window = self.map.subwin(1, 1, 0, 0)  # same as subpad
        self.player_window.refresh(0, 0, self.player_pos[0], self.player_pos[1], self.player_pos[0] + 1, self.player_pos[1] + 1)
        # self.player = self.player_window.panel

        # init map
        self._draw_map()
        self._refresh_map()

        self.last_move_time = time.time()

    def _start_loop(self):
        from simulat.core.loop import game_loop
        game_loop()

    def _map_init(self, _layout: str):
        layout = []
        for y in range(self.pad_size[0] - 1):
            line = []
            for x in range(self.pad_size[1] - 1):
                line.append(' ')
            layout.append(line)

        for y_idx, line in enumerate(_layout):
            for x_idx, char in enumerate(line):
                layout[y_idx][x_idx] = char

            # layout.append(line_list)
        return layout

    def _collision_matrix_init(self, _layout: str):
        matrix = []
        for line in _layout:
            line_list = []
            for char in line:
                if char == '#':
                    line_list.append(1)
                else:
                    line_list.append(0)
                # line_list.append(char)

            matrix.append(line_list)
        return matrix

    def _draw_map(self):
        for y, line in enumerate(self.map_layout):
            for x, char in enumerate(line):
                self.map.cs_addstr(y, x, char)

    def _refresh_map(self):
        pad_view_top = max(0, min(self.player_pos[0] - self.max_size[0] // 2, self.pad_size[0] - self.max_size[0]))
        pad_view_left = max(0, min(self.player_pos[1] - self.max_size[1] // 2, self.pad_size[1] - self.max_size[1]))

        self.map.refresh(pad_view_top, pad_view_left, 1, 0, *self.max_size)

    def _input(self, key: int):
        if key != -1:
            current_time = time.time()

            if current_time - self.last_move_time >= self.movement_delay:
                if key in [cs.KEY_LEFT, ord('h'), ord('a')]:
                    self._move_player(0, -1)
                elif key in [cs.KEY_UP, ord('k'), ord('w')]:
                    self._move_player(-1, 0)
                elif key in [cs.KEY_DOWN, ord('j'), ord('s')]:
                    self._move_player(1, 0)
                elif key in [cs.KEY_RIGHT, ord('l'), ord('d')]:
                    self._move_player(0, 1)

                self.last_move_time = current_time

    def _move_player(self, y_offset, x_offset):
        new_y = self.player_pos[0] + y_offset
        new_x = self.player_pos[1] + x_offset

        # check if out of bounds
        try:
            if new_y < 0 or new_x < 0:
                return

            self.collision_matrix[new_y][new_x]
        except IndexError:
            return

        if ((new_y, new_x)) in INTERACTIONS:
            INTERACTIONS[(new_y, new_x)]()
            return

        if not self.collision_matrix[new_y][new_x]:
            # Erase the player character from the current position
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], ' ')

            # Update player position
            self.player_pos = new_y, new_x

            # Draw the player character at the new position
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], self.player_char)

            self._refresh_map()

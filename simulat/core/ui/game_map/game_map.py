#!/usr/bin/env python3

import time
import curses as cs
import random

from typing import Final

from simulat.core.ui.windows.topbar import topbar
from simulat.core.init import stdscr

from simulat.core.init import content_win
from simulat.core.init import COLLIDER_COLOR, GRASS_COLOR, FLOOR_COLOR, INTERACTION_COLOR, INTERACTION_RADIUS_COLOR, PLAYER_COLOR, EMPTY_COLOR

from simulat.core.ui.windows.window_management.pad import Pad

from ....data.map_layouts.map_layout import MAP_LAYOUT, INTERACTIONS, TITLE


class GameMap():
    def __init__(self):
        self.MAP_SIZE: Final = 100, 100  # y, x
        self.pad_size = self.MAP_SIZE[0], self.MAP_SIZE[1]  # subject to change when user resizes terminal

        self.map_layout = self._map_init(MAP_LAYOUT)
        self.collision_matrix = self._collision_matrix_init(self.map_layout)
        self.interactions = INTERACTIONS
        self.title = TITLE
        self.movement_delay = 0.0  # seconds

        self.grass_chars = ['`', "'", '"', ',', '.', ':', ';', '!', '?']
        grass_density = 100  # lesser = more grass
        self.grass_chars.extend(' ' for _ in range(grass_density))
        self.player_char = '@'
        self.player_pos = 1, 1

        self.max_displayed_pad_size = stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1

        self.map = Pad(*self.pad_size)
        content_win.panel.replace(self.map.window)

        # set title
        topbar.title_win.clear()
        topbar.title_win.addstr(0, -1, self.title)
        topbar.title_win.refresh()

        # init map
        self._draw_map()
        self._refresh_map()

        # init player
        char_extracted = self.map.window.inch(*self.player_pos)
        self._old_chr = [chr(char_extracted & cs.A_CHARTEXT), char_extracted & cs.A_ATTRIBUTES]  # empty

        self._move_player(0, 0)

        self.last_move_time = time.time()

    def _start_loop(self):
        from simulat.core.loop import game_loop
        game_loop()

    def _map_init(self, _layout: str):
        layout = []
        for y in range(self.pad_size[0] - 1):
            line = []
            for x in range(self.pad_size[1] - 1):
                line.append('g')
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
        radius_coordinates: list = []
        for y, line in enumerate(self.map_layout):
            for x, char in enumerate(line):
                # if cell is a collider (1), draw it in COLLIDER_COLOR
                if self.collision_matrix[y][x]:
                    self.map.cs_addstr(y, x, char, COLLIDER_COLOR)

                # if cell is an interaction, store its range's coordinates in radius_coordinates
                # and draw it in INTERACTION_COLOR
                elif (y, x) in self.interactions:
                    for y_offset in [-1, 0, 1]:
                        for x_offset in [-1, 0, 1]:
                            y_radius = y + y_offset
                            x_radius = x + x_offset
                            radius_coordinates.append((y_radius, x_radius))
                    self.map.cs_addstr(y, x, char, INTERACTION_COLOR)

                # if cell is a floor, draw it in FLOOR_COLOR
                elif char == 'f':  # floor
                    self.map.cs_addstr(y, x, 'H', FLOOR_COLOR)

                # if cell is grass, draw it in GRASS_COLOR
                elif char == 'g':  # grass
                    grass_char = random.choice(self.grass_chars)
                    self.map.cs_addstr(y, x, grass_char, GRASS_COLOR)

                else:
                    self.map.cs_addstr(y, x, char, EMPTY_COLOR)

        # draw interaction radius
        for y, x in radius_coordinates:
            self.map.cs_addstr(y, x, chr(self.map.window.inch(y, x) & cs.A_CHARTEXT), INTERACTION_RADIUS_COLOR)
        # draw interactions
        for y, x in self.interactions:
            self.map.cs_addstr(y, x, chr(self.map.window.inch(y, x) & cs.A_CHARTEXT), INTERACTION_COLOR)

    def _resize(self):
        self.max_displayed_pad_size = stdscr.getmaxyx()[0] - 2, stdscr.getmaxyx()[1] - 1
        self._refresh_map()

    def _refresh_map(self):
        pad_view_top = max(0, min(self.player_pos[0] - self.max_displayed_pad_size[0] // 2, self.pad_size[0] - self.max_displayed_pad_size[0] - 1))
        pad_view_left = max(0, min(self.player_pos[1] - self.max_displayed_pad_size[1] // 2, self.pad_size[1] - self.max_displayed_pad_size[1] - 2))

        self.map.refresh(pad_view_top, pad_view_left, 1, 0, *self.max_displayed_pad_size)

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
                elif key == ord('e'):
                    self._interact()

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

        if not self.collision_matrix[new_y][new_x]:
            # Erase the player character from the current position
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], self._old_chr[0], self._old_chr[1])

            # Update player position
            self.player_pos = new_y, new_x

            # Draw the player character at the new position

            extracted = self.map.window.inch(*self.player_pos)
            attrs = extracted & cs.A_ATTRIBUTES
            char = chr(extracted & cs.A_CHARTEXT)

            self._old_chr = [char, attrs]

            # self._old_chr = self.map.window.inch(self.player_pos)

            # self._old_chr = chr(self.map.window.inch(self.player_pos[0], self.player_pos[1]))
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], self.player_char, PLAYER_COLOR)
            self._refresh_map()

    def _interact(self):
        for y_offset in [-1, 0, 1]:
            for x_offset in [-1, 0, 1]:
                y = self.player_pos[0] + y_offset
                x = self.player_pos[1] + x_offset

                if (y, x) in INTERACTIONS:
                    INTERACTIONS[(y, x)]()
                    self._refresh_map()
                    return

#!/usr/bin/env python3

import time
import curses as cs

from typing import Final

from simulat.core.ui.windows.topbar import topbar
from simulat.core.init import stdscr

from simulat.core.init import content_win
from simulat.core.init import INTERACTION_COLOR, INTERACTION_RADIUS_COLOR, PLAYER_COLOR

from simulat.core.ui.windows.window_management.pad import Pad

from ....data.map_layouts.map_layout import MAP_LAYOUT, INTERACTIONS, TITLE

from .cell.dynamic import DoorCell
from .cell.decorative import GrassCell, FloorCell
from .cell.collider import WallCell


class GameMap():
    def __init__(self):
        self.MAP_SIZE: Final = 100, 100  # y, x
        self.pad_size = self.MAP_SIZE[0] + 2, self.MAP_SIZE[1] + 2  # subject to change when user resizes terminal

        self.map = Pad(*self.pad_size)
        content_win.panel.replace(self.map.window)

        self.doors = {}
        self.interactions = INTERACTIONS

        self.title = TITLE
        self.movement_delay = 0.0  # seconds

        self.player_char = '@'
        self.player_pos = [1, 1]

        self.camera_pos = self.player_pos

        self.door_chars = {
            'd': "¬",  # door
            'D': "¬",  # closed door
            'open': "·",  # open door, will display if `self.doors[(y, x)]['open'] == True`
        }

        self.max_displayed_pad_size = stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1

        # set title
        topbar.title_win.clear()
        topbar.title_win.addstr(0, -1, self.title)
        topbar.title_win.refresh()

        # init map
        self.map_layout = self._map_init(MAP_LAYOUT)
        self.collision_matrix = self._collision_matrix_init(self.map_layout)
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
                # line.append('g')
                line.append(GrassCell(self, y, x))
            layout.append(line)

        for y_idx, line in enumerate(_layout):
            for x_idx, char in enumerate(line):
                # layout[y_idx][x_idx] = char

                # doors
                if char == "d" or char == "D":
                    layout[y_idx][x_idx] = DoorCell(self, y_idx, x_idx, locked=char == "D")
                    _door = layout[y_idx][x_idx]
                    if not _door.locked:
                        self.interactions[(y_idx, x_idx)] = _door.toggle
                    self.doors[(y_idx, x_idx)] = _door

                # walls
                elif char == "#":
                    layout[y_idx][x_idx] = WallCell(self, y_idx, x_idx)

                # floor
                elif char == "f":
                    layout[y_idx][x_idx] = FloorCell(self, y_idx, x_idx)

                # grass
                elif char == "g":
                    layout[y_idx][x_idx] = GrassCell(self, y_idx, x_idx)

                # # empty
                # else:
                #     layout[y_idx][x_idx] = Cell(self, y_idx, x_idx)

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
                # if self.collision_matrix[y][x]:
                #     self.map.cs_addstr(y, x, char, COLLIDER_COLOR)

                # if cell is an interaction, store its range's coordinates in radius_coordinates
                # and draw it in INTERACTION_COLOR
                if (y, x) in self.interactions:
                    for y_offset in [-1, 0, 1]:
                        for x_offset in [-1, 0, 1]:
                            y_radius = y + y_offset
                            x_radius = x + x_offset
                            radius_coordinates.append((y_radius, x_radius))
                    self.map.cs_addstr(y, x, str(char), INTERACTION_COLOR)

                char.draw()
        self._refresh_map()

        # draw interaction radius
        for y, x in radius_coordinates:
            self.map.cs_addstr(y, x, chr(self.map.window.inch(y, x) & cs.A_CHARTEXT), INTERACTION_RADIUS_COLOR)
        # draw interactions
        for y, x in self.interactions:
            self.map.cs_addstr(y, x, chr(self.map.window.inch(y, x) & cs.A_CHARTEXT), INTERACTION_COLOR)

        self._draw_dynamic()

    def _draw_dynamic(self):
        # draw doors
        for door in self.doors:
            self.doors[door].update()
            self.doors[door].draw()
        self._refresh_map()

    def _resize(self):
        self.max_displayed_pad_size = stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1
        self._refresh_map()

    def _refresh_map(self):
        pad_view_top = max(0, min(self.camera_pos[0] - self.max_displayed_pad_size[0] // 2, self.pad_size[0] - self.max_displayed_pad_size[0] - 1))
        pad_view_left = max(0, min(self.camera_pos[1] - self.max_displayed_pad_size[1] // 2, self.pad_size[1] - self.max_displayed_pad_size[1] - 2))

        self.map.refresh(pad_view_top, pad_view_left, 1, 0, *self.max_displayed_pad_size)

    def _toggle_all_doors(self):
        for door in self.doors:
            self.doors[door].toggle()
        self._draw_dynamic()

    def _input(self, key: int):
        if key != -1:
            current_time = time.time()

            if current_time - self.last_move_time >= self.movement_delay:
                if key in [ord('h'), ord('a')]:
                    self._move_player(0, -1)
                    self.camera_pos = self.player_pos
                elif key in [ord('k'), ord('w')]:
                    self._move_player(-1, 0)
                    self.camera_pos = self.player_pos
                elif key in [ord('j'), ord('s')]:
                    self._move_player(1, 0)
                    self.camera_pos = self.player_pos
                elif key in [ord('l'), ord('d')]:
                    self._move_player(0, 1)
                    self.camera_pos = self.player_pos
                elif key == cs.KEY_LEFT:
                    self._move_camera(0, -1)
                elif key == cs.KEY_UP:
                    self._move_camera(-1, 0)
                elif key == cs.KEY_DOWN:
                    self._move_camera(1, 0)
                elif key == cs.KEY_RIGHT:
                    self._move_camera(0, 1)
                elif key == ord('e'):
                    self._interact()

                self.last_move_time = current_time

    def _move_camera(self, y_offset, x_offset):
        self.camera_pos[0] += y_offset
        self.camera_pos[1] += x_offset
        self._refresh_map()

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

        # if self.doors.get((new_y, new_x)):
        #     if not self.doors[(new_y, new_x)].open:
        #         return

        if self.map_layout[new_y][new_x].collider:
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

        topbar.details_win.clear()
        topbar.details_win.addstr(0, -1, f"y: {self.player_pos[0]}, x: {self.player_pos[1]}")
        topbar.details_win.refresh()

    def _interact(self):
        closest_interaction = None
        closest_distance = float('inf')  # Initialize with a large value

        for y_offset in [-1, 0, 1]:
            for x_offset in [-1, 0, 1]:

                y = self.player_pos[0] + y_offset
                x = self.player_pos[1] + x_offset

                if (y, x) in self.interactions:
                    if self.doors.get((y, x)) and y_offset == 0 and x_offset == 0:
                        return  # don't interact with doors when standing on them

                    distance = ((self.player_pos[0] - y) ** 2 + (self.player_pos[1] - x) ** 2) ** 0.5
                    if distance < closest_distance:
                        closest_interaction = (y, x)
                        closest_distance = distance

        if closest_interaction is not None:
            self.interactions[closest_interaction]()
            self._draw_dynamic()
            self._refresh_map()

#!/usr/bin/env python3

import time
import curses as cs

from typing import Final

from simulat.core.init.init_ui import stdscr, topbar, wrapper_win, content_win

from simulat.core.init.init_colors import INTERACTION_COLOR, INTERACTION_RADIUS_COLOR, PLAYER_COLOR

from simulat.core.ui.windows.window_management.pad import Pad

from ....data.map_layouts.map_layout import MAP_LAYOUT, INTERACTIONS, TITLE

from .cell.dynamic import DoorCell
from .cell.decorative import GrassCell, FloorCell
from .cell.collider import WallCell


class GameMap():
    """
    The `GameMap` class represents the map of the game. It provides
    functionality for creating, displaying and interacting with
    the game world, including features such as movement, collision, doors
    and interactions.

    Attributes:
        MAP_SIZE (tuple): The size of the map in cells.
        pad_size (tuple): The size of the map in cells, plus 2 for the border.
        map (Pad): The map's pad.
        doors (dict): A dictionary of all the doors in the map.
        interactions (dict): A dictionary of all the interactions in the map.
        title (str): The title of the map.
        movement_delay (float): The delay between each movement in seconds.
        player_char (str): The character representing the player.
        player_pos (list): The position of the player in the map.
        camera_pos (list): The position of the camera in the map.
        door_chars (dict): A dictionary of all the characters representing doors.
        max_displayed_pad_size (tuple): The maximum size of the map that can be displayed on the screen.
        map_layout (list): A list of lists representing the map layout.
        collision_matrix (list): A list of lists representing the map's collision matrix.
        _old_chr (list): The character that was previously at the player's position.
        last_move_time (float): The time of the last movement.

    Methods:
        _start_loop: Starts the game loop.
        _map_init: Initializes the map.
        _collision_matrix_init: Initializes the collision matrix.
        _draw_map: Draws the map.
        _draw_dynamic: Draws the dynamic elements of the map.
        _resize: Resizes the map.
        _refresh_map: Refreshes the map.
        _toggle_all_doors: Toggles all the doors in the map.
        _input: Handles input.
        _move_camera: Moves the camera.
        _move_player: Moves the player.
        _interact: Interacts with the closest interaction.
    """
    def __init__(self):
        """Initializes the `GameMap` class."""
        self.MAP_SIZE: Final = 100, 100  # y, x
        self.pad_size = self.MAP_SIZE[0] + 2, self.MAP_SIZE[1] + 2

        self.map = Pad(*self.pad_size)
        content_win.panel.replace(self.map.window)

        self.doors = {}
        self.interactions = INTERACTIONS

        self.title = TITLE
        self.movement_delay = 0.0  # seconds

        self.player_char = '@'
        self.player_pos = [1, 1]

        self.camera_pos = [1, 1]

        self.door_chars = {
            'd': "¬",  # door
            'D': "¬",  # closed door
            'open': "·",  # open door, will display if `self.doors[(y, x)]['open'] == True`
        }

        self.max_displayed_pad_size = wrapper_win.getmaxyx()[0] - 1, wrapper_win.getmaxyx()[1] - 1

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
        """Starts the game loop."""
        from simulat.core.loop import game_loop
        game_loop()

    def _map_init(self, _layout: str):
        """Initializes the map.

        Initializes the map by iterating through the map layout and creating
        the corresponding cells. Also initializes the interactions and doors
        dictionaries.
        If the defined map size (`self.MAP_SIZE`) is bigger than the map layout,
        the rest of the map will be filled with `GrassCell`s.

        Characters:
            - `d`: door, a dynamic cell that can be opened and closed (toggled)
            when closed, is a collider;
            - `D`: locked door, a dynamic cell that cannot be toggled, and is
            a collider;
            - `#`: wall, a non-togglable static collider;
            - `f`: floor, a decorative cell, not a collider;
            - `g`: grass, a decorative cell, not a collider;

        Note: Doors do not impact the collision matrix
        (see `self._collision_matrix_init`), as they are dynamic
        and can be toggled.

        Args:
            _layout (str): The map layout.
        """
        layout = []
        for y in range(self.pad_size[0] - 1):
            line = []
            for x in range(self.pad_size[1] - 1):
                line.append(GrassCell(self, y, x))
            layout.append(line)

        for y_idx, line in enumerate(_layout):
            for x_idx, char in enumerate(line):

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

        return layout

    def _collision_matrix_init(self, _layout: str):
        """Initializes the collision matrix.

        Collision matrix is a matrix of 1s and 0s, where 1 represents a collider
        and 0 represents an empty cell. Will be used for pathfinding.

        Note: Doors do not impact the collision matrix, as they are dynamic
        and can be toggled.

        Args:
            _layout (str): The map layout.
        """
        matrix = []
        for line in _layout:
            line_list = []
            for char in line:
                if char == '#':
                    line_list.append(1)
                else:
                    line_list.append(0)

            matrix.append(line_list)
        return matrix

    def _draw_map(self):
        """Draws the map.

        Draws the map by iterating through the map layout and drawing each cell.
        Interactions are drawn in `INTERACTION_COLOR`, and their radius is drawn
        in `INTERACTION_RADIUS_COLOR`.

        Note: Doors are not drawn here, as they are dynamic and drawn in
        `self._draw_dynamic`.
        """
        radius_coordinates: list = []
        for y, line in enumerate(self.map_layout):
            for x, char in enumerate(line):
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
        """Draws the dynamic elements of the map.

        Draws the dynamic elements of the map, such as doors.

        Note: This method is called only on initialization and by `self._toggle_all_doors`.
        """
        # draw doors
        for door in self.doors:
            self.doors[door].update()
            self.doors[door].draw()
        self._refresh_map()

    def _resize(self):
        """Resizes the map to fit the terminal size."""
        self.max_displayed_pad_size = wrapper_win.getmaxyx()[0] - 1, wrapper_win.getmaxyx()[1] - 1
        self._refresh_map()

    def _refresh_map(self):
        """Refreshes the map.

        Refreshes the map by refreshing the pad view to fit the camera position
        (centered or not, depends on player position, e.g. near the map border).
        """
        pad_view_top = max(0, min(self.camera_pos[0] - self.max_displayed_pad_size[0] // 2, self.pad_size[0] - self.max_displayed_pad_size[0] - 1))
        pad_view_left = max(0, min(self.camera_pos[1] - self.max_displayed_pad_size[1] // 2, self.pad_size[1] - self.max_displayed_pad_size[1] - 2))

        self.map.refresh(pad_view_top, pad_view_left, 1, 0, *self.max_displayed_pad_size)

    def _toggle_all_doors(self):
        """Toggles all the doors in the map.

        Toggles all the doors in the map, and redraws them.
        """
        for door in self.doors:
            self.doors[door].toggle()
        self._draw_dynamic()

    def _input(self, key: int):
        """Handles input.

        Handles input by moving the player, moving the camera, or interacting
        with the closest interaction.

        Args:
            key (int): The key pressed.

        Note: The movement delay works by storing the time of the last movement
        in `self.last_move_time`, and comparing it to the current time.
        """
        if key != -1:
            current_time = time.time()

            if current_time - self.last_move_time >= self.movement_delay:
                if key in [ord('h'), ord('a')]:
                    self._move_player(0, -1)
                elif key in [ord('k'), ord('w')]:
                    self._move_player(-1, 0)
                elif key in [ord('j'), ord('s')]:
                    self._move_player(1, 0)
                elif key in [ord('l'), ord('d')]:
                    self._move_player(0, 1)
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
        """Moves the camera.

        Moves the camera by `y_offset` and `x_offset`, and refreshes the map.
        """
        self.camera_pos[0] += y_offset
        self.camera_pos[1] += x_offset
        self._refresh_map()

    def _move_player(self, y_offset, x_offset):
        """Moves the player.

        Checks if the player can move by `y_offset` and `x_offset`, and if so,
        moves the player and the camera and refreshes the map.

        Args:
            y_offset (int): The y offset to move by.
            x_offset (int): The x offset to move by.
        """
        new_y = self.player_pos[0] + y_offset
        new_x = self.player_pos[1] + x_offset

        # check if out of bounds
        try:
            if new_y < 0 or new_x < 0:
                return

            self.collision_matrix[new_y][new_x]
        except IndexError:
            return

        if self.map_layout[new_y][new_x].collider:
            return

        if not self.collision_matrix[new_y][new_x]:
            # draws the old character with the old attributes at the old position,
            # to avoid leaving a trail of characters behind the player, effectively
            # erasing the player's previous position
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], self._old_chr[0], self._old_chr[1])

            # update the player's position
            self.player_pos[0] = new_y
            self.player_pos[1] = new_x

            # update the camera's position
            self.camera_pos[0] = new_y
            self.camera_pos[1] = new_x

            # extract the character and attributes at the player's position
            # and store them in `self._old_chr`` to be drawn on the next move
            extracted = self.map.window.inch(*self.player_pos)
            attrs = extracted & cs.A_ATTRIBUTES
            char = chr(extracted & cs.A_CHARTEXT)

            self._old_chr = [char, attrs]

            # draw the player character at the new position in `PLAYER_COLOR`
            # and refresh the map
            self.map.cs_addstr(self.player_pos[0], self.player_pos[1], self.player_char, PLAYER_COLOR)
            self._refresh_map()

        topbar.update_details(f"y: {self.player_pos[0]}, x: {self.player_pos[1]}")

    def _interact(self):
        """Interacts with the closest interaction.

        Interacts with the closest interaction by iterating through the
        interactions dictionary and finding the closest one.
        """
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

#!/usr/bin/env python3

from simulat.core.init.init_colors import DOOR_COLOR, LOCKED_DOOR_COLOR

from .cell import Cell

door_cells = {
    'unlocked': "¬",  # door
    'locked': "¬",  # locked door
    'open': "·",  # open door
}


class DoorCell(Cell):
    def __init__(self, _map, y: int, x: int, /, locked: bool, _open: bool = False):
        super().__init__(_map, y, x)

        self.open = _open
        self.locked = locked

        self.collider = not self.open

        self.update()  # set self.char and self.attr
        # self.draw()

    def update(self):
        if self.open:
            self.char = door_cells['open']
            self.attr = DOOR_COLOR
        elif self.locked:
            self.char = door_cells['locked']
            self.attr = LOCKED_DOOR_COLOR
        else:
            self.char = door_cells['unlocked']
            self.attr = DOOR_COLOR

    def toggle(self):
        self.open = not self.open
        self.collider = not self.open
        self.update()
        self.draw()

    def __repr__(self):
        return f"<DoorCell y={self.y} x={self.x} open={self.open} locked={self.locked}>"

    def __str__(self) -> str:
        return self.char

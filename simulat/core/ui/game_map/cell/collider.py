#!/usr/bin/env python3

from simulat.core.init import COLLIDER_COLOR

from .cell import Cell


class ColliderCell(Cell):
    def __init__(self, _map, y: int, x: int):
        super().__init__(_map, y, x)
        self.attr = COLLIDER_COLOR
        self.collider = True

    def __repr__(self):
        return f"<ColliderCell y={self.y} x={self.x}>"


class WallCell(ColliderCell):
    def __init__(self, _map, y: int, x: int):
        super().__init__(_map, y, x)

        self.char = "#"

        # self.draw()

    def __repr__(self):
        return f"<WallCell y={self.y} x={self.x}>"

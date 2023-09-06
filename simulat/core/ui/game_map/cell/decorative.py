#!/usr/bin/env python3

import random as rn

from simulat.core.init import GRASS_COLOR, FLOOR_COLOR

from .cell import Cell

floor_chars = ['.', '_', '-']
floor_density = 15  # lesser = more knots
floor_chars.extend(' ' for _ in range(floor_density))

grass_chars = ['`', "'", '"', ',', '.', ':', ';', '|', '¦']
grass_density = 100  # lesser = more grass
grass_chars.extend(' ' for _ in range(grass_density))


class DecorativeCell(Cell):
    def __init__(self, _map, y: int, x: int):
        super().__init__(_map, y, x)

        self.collider = False

    def __repr__(self):
        return f"<DecorativeCell y={self.y} x={self.x}>"


class FloorCell(DecorativeCell):
    def __init__(self, _map, y: int, x: int):
        super().__init__(_map, y, x)

        self.char = rn.choice(floor_chars)
        self.attr = FLOOR_COLOR

        # self.draw()

    def __repr__(self):
        return f"<FloorCell y={self.y} x={self.x}>"


class GrassCell(DecorativeCell):
    def __init__(self, _map, y: int, x: int):
        super().__init__(_map, y, x)

        self.char = rn.choice(grass_chars)
        self.attr = GRASS_COLOR

        # self.draw()

    def __repr__(self):
        return f"<GrassCell y={self.y} x={self.x}>"


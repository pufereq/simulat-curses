#!/usr/bin/env python3


class Door:
    def __init__(self, y: int, x: int, /, locked: bool, open: bool = False, timeout: int = 3):
        self.y = y
        self.x = x
        self.open = open
        self.locked = locked

    def toggle(self):
        from simulat.core.init import game_map
        self.open = not self.open
        game_map._draw_dynamic()  # may be optimized

    def __str__(self):
        return f"Door at ({self.y}, {self.x}), {self.open=}, {self.locked=}"

    def __repr__(self):
        return {'y': self.y, 'x': self.x, 'open': self.open, 'locked': self.locked}

#!/usr/bin/env python3


door_chars = {
    'd': "¬",  # door
    'D': "¬",  # closed door
    'open': "·",  # open door, will display if `self.doors[(y, x)]['open'] == True`
}


class Cell():
    def __init__(self, _map, y: int, x: int):
        self.map = _map
        self.y = y
        self.x = x

    def draw(self, /, refresh: bool = False):
        self.map.map.cs_addstr(self.y, self.x, self.char, self.attr)
        if refresh:
            self.map._refresh_map()

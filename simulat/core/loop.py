#!/usr/bin/env python3

# from main import
def game_loop():
    from simulat.core.init import game_map
    while True:
        game_map._input()

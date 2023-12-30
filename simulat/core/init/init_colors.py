#!/usr/bin/env python3

import curses as cs


def init_colors():
    global COLLIDER_COLOR, GRASS_COLOR, FLOOR_COLOR, INTERACTION_COLOR, INTERACTION_RADIUS_COLOR, PLAYER_COLOR, EMPTY_COLOR, DOOR_COLOR, LOCKED_DOOR_COLOR
    COLLIDER_PAIR: int = 1
    GRASS_PAIR: int = 2
    FLOOR_PAIR: int = 3
    INTERACTION_PAIR: int = 4
    INTERACTION_RADIUS_PAIR: int = 5
    PLAYER_PAIR: int = 6
    EMPTY_PAIR: int = 7
    DOOR_PAIR: int = 8
    LOCKED_DOOR_PAIR: int = 9

    COLOR_TRANSPARENT: int = -1

    # colors
    COLOR_BLACK: int = 0
    COLOR_RED: int = 1
    COLOR_GREEN: int = 2
    COLOR_YELLOW: int = 3
    COLOR_BLUE: int = 4
    COLOR_MAGENTA: int = 5
    COLOR_CYAN: int = 6
    COLOR_WHITE: int = 7
    COLOR_GRAY: int = 8

    # bright colors
    COLOR_BRIGHT_RED: int = 9
    COLOR_BRIGHT_GREEN: int = 10
    COLOR_BRIGHT_YELLOW: int = 11
    COLOR_BRIGHT_BLUE: int = 12
    COLOR_BRIGHT_MAGENTA: int = 13
    COLOR_BRIGHT_CYAN: int = 14
    COLOR_BRIGHT_WHITE: int = 15

    # other colors
    COLOR_BROWN: int = 136
    COLOR_DARK_BROWN: int = 94
    COLOR_GRASS_GREEN: int = 22

    cs.start_color()
    cs.use_default_colors()

    cs.init_pair(COLLIDER_PAIR, COLOR_GRAY, COLOR_WHITE)
    cs.init_pair(GRASS_PAIR, COLOR_GREEN, COLOR_GRASS_GREEN)
    cs.init_pair(FLOOR_PAIR, COLOR_DARK_BROWN, COLOR_BROWN)
    cs.init_pair(INTERACTION_PAIR, COLOR_CYAN, COLOR_CYAN)
    cs.init_pair(INTERACTION_RADIUS_PAIR, COLOR_BRIGHT_CYAN, COLOR_BRIGHT_BLUE)
    cs.init_pair(PLAYER_PAIR, COLOR_BRIGHT_MAGENTA, COLOR_TRANSPARENT)
    cs.init_pair(EMPTY_PAIR, COLOR_WHITE, COLOR_TRANSPARENT)
    cs.init_pair(DOOR_PAIR, COLOR_YELLOW, COLOR_DARK_BROWN)
    cs.init_pair(LOCKED_DOOR_PAIR, COLOR_BLACK, COLOR_DARK_BROWN)

    COLLIDER_COLOR = cs.color_pair(COLLIDER_PAIR) | cs.A_NORMAL
    GRASS_COLOR = cs.color_pair(GRASS_PAIR)
    FLOOR_COLOR = cs.color_pair(FLOOR_PAIR)
    INTERACTION_COLOR = cs.color_pair(INTERACTION_PAIR)
    INTERACTION_RADIUS_COLOR = cs.color_pair(INTERACTION_RADIUS_PAIR)
    PLAYER_COLOR = cs.color_pair(PLAYER_PAIR) | cs.A_BOLD
    EMPTY_COLOR = cs.color_pair(EMPTY_PAIR)
    DOOR_COLOR = cs.color_pair(DOOR_PAIR) | cs.A_BOLD
    LOCKED_DOOR_COLOR = cs.color_pair(LOCKED_DOOR_PAIR) | cs.A_BOLD
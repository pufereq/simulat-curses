#!/usr/bin/env python3

from typing import Final

from main import test

TITLE: Final = "MAP"

MAP_LAYOUT: Final = [
    "###############################",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffffd",
    "#fffffffffffffffffffffffffffffd",
    "#fffffffffffffffffffffffffffffd",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "#fffffffffffffffffffffffffffff#",
    "###############DD##############"
]


def example_action():
    from simulat.core.init import game_map
    game_map._toggle_all_doors()


INTERACTIONS: Final = {
    (2, 1): example_action,
    (5, 5): test,
}

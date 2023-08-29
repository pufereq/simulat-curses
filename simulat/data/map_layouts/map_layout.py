#!/usr/bin/env python3

from typing import Final

TITLE: Final = "MAP"

MAP_LAYOUT: Final = [
    "###############################",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                              ",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "#                             #",
    "###############################"
]


def example_action():
    raise Exception("you have found an example action!")


INTERACTIONS: Final = {
    (2, 1): example_action,
}

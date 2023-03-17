<!-- markdownlint-disable MD033 MD041 -->

<div align="center">
    <summary>
        <h1 style="display: inline-block;">simulat</h1>
        &nbsp
        it's all lowercase!
    </summary>
</div>

<div align="center">
    <a href="https://github.com/pufereq/simulat/blob/main/LICENSE">
        <img alt="LICENSE" src=https://img.shields.io/github/license/pufereq/simulat>
    </a>
    <a href="https://github.com/pufereq/simulat/graphs/commit-activity">
        <img alt="Maintained" src="https://img.shields.io/maintenance/yes/2023">
    </a>
    <a href="https://github.com/pufereq/simulat/graphs/contributors">
        <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/pufereq/simulat">
    </a>
    <a href="https://github.com/pufereq/simulat/pulse">
        <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/pufereq/simulat">
    </a>
    <a href="https://github.com/pufereq/simulat">
        <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/pufereq/simulat">
    </a>
    <br>
    <a href="https://github.com/pufereq/simulat/releases">
        <img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/pufereq/simulat?sort=semver">
        <img alt="GitHub release (latest SemVer including pre-releases)" src="https://img.shields.io/github/v/release/pufereq/simulat?include_prereleases&sort=semver&label=pre-release">
    </a>
</div>
<!-- markdownlint-enable MD041 -->

---

## Table of Contents

- [General Information](#general-information)
- [The Idea](#the-idea)
- [Features](#features)
- [Dependencies](#features)
- [Installation](#installation)
- [License](#license)
- [Acknowledgments](#acknowledgments)
<!-- TODO -->

## General Information

simulat is a CLI curses-based life simulator game.
<br>
I undertook this project because I saw that there are _almost_ no games
running in the terminal _...and I was bored_.

## The Idea

The idea for simulat came from The Sims.
I started coding [simulat-old](https://github.com/pufereq/simulat-old) in May 2022
then using the [`rich`](https://github.com/Textualize/rich) library but
felt restricted by no ability to refresh stats, advance game time without
always typing `ENTER`.
<br>
That's when I saw a [YouTube video of OldenRPG by Luis Perez](https://www.youtube.com/watch?v=DX1a8Uz12Xc).
Fascinated by it I started learning about the `curses` library.
<br>
...and here we are!

## Features

none yet

## Dependencies

None

## Installation

Clone the Git repository using:

```sh
git clone https://github.com/pufereq/simulat
```

<!-- Install dependencies
```sh
pip install -r requirements.txt
``` -->
Done! Run the game:

```sh
python3 main.py
```

## License

This software is licensed under [GNU GPLv3](LICENSE).

## Acknowledgments

Inspired by

- [The Sims](https://www.ea.com/games/the-sims)
- [OldenRPG](https://youtube.com/watch?v=DX1a8Uz12Xc)

# Changelog

All notable changes to this project will be documented in this file.

## [0.5.0-alpha.3] - 2023-10-29

### Documentation

- [`eea54ee`](https://github.com/pufereq/simulat/commit/eea54eef4be70fcf6ce12ff0aa1216f3d71983b6) **menu_widget.py**: Remove Args section from class docstring

### Features

- [`dcc184b`](https://github.com/pufereq/simulat/commit/dcc184b2583061d5158318e5c8a47c42f917d8bc) **menu_widget.py**: Add `locked_msg` argument and display it when selecting a locked entry

### Miscellaneous Tasks

- [`06ad077`](https://github.com/pufereq/simulat/commit/06ad077bc4385cae5e082948b668e16dfa8a9ec3) **release_it.yml**: Update release_it workflow to use git-cliff
- [`167fe61`](https://github.com/pufereq/simulat/commit/167fe612aa6d956c9e812cd05f78ea066e5c9200) **.release-it.toml**: Modify calls to now point to git-cliff
- [`b8b72e6`](https://github.com/pufereq/simulat/commit/b8b72e6538bcdc5c4eae4e1515b859805ce81879) **cliff.toml**: Add git-cliff configuration file `cliff.toml`
- [`3f0533f`](https://github.com/pufereq/simulat/commit/3f0533f24acf924f238ae50f8e3a2339230fd150) **.cz.toml**: Remove `.cz.toml`
- [`b1cab52`](https://github.com/pufereq/simulat/commit/b1cab521ca68fc0756b49cdab5d14d66e7d2f821) **menu_widget.py**: Make new game `MenuEntry` locked
- [`9abef55`](https://github.com/pufereq/simulat/commit/9abef55e5f9bc88966f44871c886262aee04530c) **widget.py**: Adjust widget size based on parent's `description` variable
- [`eeba2fa`](https://github.com/pufereq/simulat/commit/eeba2fa4ab575f738e03dc46f1527125105f6e2e) **container.py**: Set description to an empty string if None instead of `No description provided.`
- [`57e9daf`](https://github.com/pufereq/simulat/commit/57e9daf42741edf2a869b15f4258a102f0490b76) **menu_widget.py**: Disable confirming locked entries
- [`20ec781`](https://github.com/pufereq/simulat/commit/20ec781934984385f38cf29ab608549bf064f5ed) **menu_widget.py**: Prepend `locked:` to info of locked entry

### Styling

- [`7ba5ff9`](https://github.com/pufereq/simulat/commit/7ba5ff97714e233b325f4f6a4db9cb9616e4a4b2) **menu_widget.py**: Improve code formatting in MenuEntry constructor

## [0.5.0-alpha.2] - 2023-10-26

### Bug Fixes

- [`76b4628`](https://github.com/pufereq/simulat/commit/76b462843ab2d440212172d6258a8b32c609ef53) **container.py**: Fix `loop()` not using result included in `WidgetEndLoop` exception

### Features

- [`4cea9b5`](https://github.com/pufereq/simulat/commit/4cea9b5882d37275c0373646b68d1cd5617844f5) **text_input_widget.py**: Add `TextInputWidget` class

### Miscellaneous Tasks

- [`389abb3`](https://github.com/pufereq/simulat/commit/389abb3afd1d8a661baf93437740595999730285) **release**: 0.5.0-alpha.2
- [`30a8c66`](https://github.com/pufereq/simulat/commit/30a8c661860b047d1b463603e1cd599618ecb1db) **release-it.toml**: Fix error when generating changelog
- [`067a20d`](https://github.com/pufereq/simulat/commit/067a20d2822b61c56894f9ac6781ec120b0d3212) **release_it.yml**: Fix error when generating changelog
- [`af27c09`](https://github.com/pufereq/simulat/commit/af27c09c58c368d25ea180454f61d33f59c9989b) **container.py**: Remove debug call to `move_relative` with `d` key
- [`0c8d9a2`](https://github.com/pufereq/simulat/commit/0c8d9a262217fde468c729a934abd5331da6ada0) **main.py**: Add menu entry for debugging text input widget

## [0.5.0-alpha.1] - 2023-10-22

### Bug Fixes

- [`8e36742`](https://github.com/pufereq/simulat/commit/8e36742a86194cb6be5ea2f2593f5acb46928ba1) **container.py**: Fix error when calling `move` method of `Container` class
- [`f990188`](https://github.com/pufereq/simulat/commit/f99018897f7173da5294c4452d4025c762c41077) **menu_widget.py**: Fix TypeError when `None` provided as `info` argument in `MenuEntry`
- [`71b6037`](https://github.com/pufereq/simulat/commit/71b6037ab1257ca4b80d054dfb0017cf42fa55ff) **menu_widget.py**: Fix TypeError when `None` provided as `description`
- [`13b1939`](https://github.com/pufereq/simulat/commit/13b19392067cbbf6f35e751e1506290c826262fa) **container.py**: Fix visual glitch when moving the container
- [`b011ac8`](https://github.com/pufereq/simulat/commit/b011ac803ab29ff25aa191d135357cc7ff9c6dbc) **menu_widget.py**: Fix selection bugging out when `self.items` is smaller than `self.MENU_SIZE`
- [`af1b4df`](https://github.com/pufereq/simulat/commit/af1b4df53215fb86de066317a3a9d281eea8234f) **window.py**: Fix wrong `beg_y` and `beg_x` being set when `update_size()` called
- [`4b5c67e`](https://github.com/pufereq/simulat/commit/4b5c67e00cabb1da4bce00af325bea1f34380ba1) **container.py**: Fix info details appearing only for 0.1 seconds while `GameMap` loaded
- [`a2597bb`](https://github.com/pufereq/simulat/commit/a2597bbdadc9f23a62547e5bb0e0746a174decd3) **main.py**: Fix typo in import in `test()`
- [`1a69b6b`](https://github.com/pufereq/simulat/commit/1a69b6b6da6f76d7d3ae803eb4dcd3e93944033d) Fix double init of curses
- [`b27ffcc`](https://github.com/pufereq/simulat/commit/b27ffcc6415d1c3e3853c023a12809b892a0ed4b) **window.py**: Fix error when `set_title()` calls `window.refresh()` if it's a pad
- [`fa620f8`](https://github.com/pufereq/simulat/commit/fa620f8c4e2b52117bbcfd0cd86f61a4e1743417) **window.py**: Fix error when using `addstr()` with `-1` as `y` or `x`

### Documentation

- [`f98a9b4`](https://github.com/pufereq/simulat/commit/f98a9b40daaadcdd7436bd46c82b737072db8bfa) **loop.py**: Add docstrings to `game_loop()` and `_loop()`
- [`5eeae4d`](https://github.com/pufereq/simulat/commit/5eeae4d54dc372d7d498eac2fe86f1487e1316fb) **container.py**: Add docstrings to `Container` class
- [`31e5f57`](https://github.com/pufereq/simulat/commit/31e5f57ead3bbd5ca00d2a4bab323a123fb07449) **widget.py**: Add docstrings to `Widget` class
- [`00ddbca`](https://github.com/pufereq/simulat/commit/00ddbca79d09d15a113f3e0a24bb6c9cd75d5022) **menu_widget.py**: Add docstrings to `MenuWidget` class
- [`cdb4b43`](https://github.com/pufereq/simulat/commit/cdb4b4320b0bac26e583d12a8ba94d50a7e55bec) **menu_widget.py**: Add docstrings to `MenuEntry` class
- [`69fe85c`](https://github.com/pufereq/simulat/commit/69fe85cc5758c765ba1add0147edc22f7054765f) **game_map.py**: Remove incorrect comment
- [`188a61b`](https://github.com/pufereq/simulat/commit/188a61b4a9eecf311ba4db2f40678f1422381528) **game_map.py**: Modify comments in `_move_player` method to improve readability
- [`a590dc6`](https://github.com/pufereq/simulat/commit/a590dc66375d22fa4c3a5683235b92ba562e1983) **game_map.py**: Add docstrings

### Features

- [`9ef9f0a`](https://github.com/pufereq/simulat/commit/9ef9f0afa8a0b75c5222db7a6afb7e352cea40d9) **menu_widget.py**: Make `self.MENU_SIZE` dependent on widget's size
- [`5578607`](https://github.com/pufereq/simulat/commit/5578607f3b87020089d9486aca38974e07812ea6) **container.py**: Add `description` field to `Container` class constructor
- [`dd661bf`](https://github.com/pufereq/simulat/commit/dd661bf975b9f205c1b96b007e755a6a74c04e0f) **menu_widget.py**: Add `_display_info` method
- [`4c332e3`](https://github.com/pufereq/simulat/commit/4c332e3bb7f99af206be198a72e37527c1f081b4) **menu_widget.py**: Add vim keybindings (`j` (down) & `k` (up)) to `_input`
- [`1414dcb`](https://github.com/pufereq/simulat/commit/1414dcb351643eeff416e3035f7a13a86d37aa50) **menu_widget.py**: Add ability to change selection using `PageUp` and `PageDown`
- [`20885e3`](https://github.com/pufereq/simulat/commit/20885e352a4ef2349dba2337f1f0fbb1b685dcb6) **main.py**: Modify `test()` to now use `MenuWidget` instead of `DebugWidget`
- [`7347bdd`](https://github.com/pufereq/simulat/commit/7347bddb0aae639c78da2d3df98f23056ab1554f) **menu_widget.py**: Add a `MenuWidget` class.
- [`e831f05`](https://github.com/pufereq/simulat/commit/e831f05121597ca7dc1d67550e263be4a932541c) **container.py**: Add a `loop` method
- [`45a0276`](https://github.com/pufereq/simulat/commit/45a0276833085e512d3367f7969fab9ee1be4558) **container.py**: Add `move_relative` method
- [`269e85d`](https://github.com/pufereq/simulat/commit/269e85df76d6ed54ad2937f7da8034bf91a5a002) **container.py**: Add `move` method with centering functionality
- [`64824f7`](https://github.com/pufereq/simulat/commit/64824f71d065b19d37ee9a3b5455ab6381b1d5ec) **container.py**: Modify name of `draw_widget` to `refresh_all`
- [`dc04e3c`](https://github.com/pufereq/simulat/commit/dc04e3c77fffff80b8921e00e7b48c3adb28cd31) **widget.py**: Add `WidgetLoopEnd` Exception class
- [`4bc1d70`](https://github.com/pufereq/simulat/commit/4bc1d70b31b39dd6fb7d1e8bc14593418923e9d9) **widget.py**: Add `_wrap_str_to_width` method
- [`b8a4557`](https://github.com/pufereq/simulat/commit/b8a4557e93b447022ba2aa358809d46aece21da4) **window.py**: Add `mvwin` method
- [`4e8f810`](https://github.com/pufereq/simulat/commit/4e8f81099fbd42d7cb5417584eb61ea0b96a3c1a) **window.py**: Add `erase` method
- [`91adde7`](https://github.com/pufereq/simulat/commit/91adde7850abf25565371c6b724d74708bdaf294) **window.py**: Add call to `update_size` in `refresh`
- [`7c4c5d0`](https://github.com/pufereq/simulat/commit/7c4c5d064a73979d83744abcff38ebaa3cd27c94) **window.py**: Add `update_size` method
- [`f8aea86`](https://github.com/pufereq/simulat/commit/f8aea867c31bd937460e04a8a5089d941a397364) **window.py**: Add `self.beg_y` and `self.beg_x` variables
- [`662f957`](https://github.com/pufereq/simulat/commit/662f95785bd076c7cb7daf8262e4780224a79397) **window.py**: Add call to `self.keypad(True)` in `_common_init()`
- [`9f2097f`](https://github.com/pufereq/simulat/commit/9f2097fa864be28f6ec6989220fc8bc16ae63f5b) **map_layout.py**: Add call to `main.test()`(the example container) from the `GameMap`
- [`c7bd0a4`](https://github.com/pufereq/simulat/commit/c7bd0a40249b2cdef4a65dbddce5a987f00c2acb) **container.py**: Add centering of the container relative to `content_win`
- [`2a2a58f`](https://github.com/pufereq/simulat/commit/2a2a58f18c722a223dfac4583719b954aae2fe4c) **main.py**: Move example container to its own function
- [`bb1928d`](https://github.com/pufereq/simulat/commit/bb1928dbfe98c03a58cbefdb0ce7e49f33e19928) **main.py**: Add a 'container' button for debugging purposes
- [`d95d230`](https://github.com/pufereq/simulat/commit/d95d230b83d442c0bdb93d9ec621ab74bb2a3723) **debug_widget.py**: Add a `DebugWidget` for debugging of `Container` and `Widget` classes
- [`ee340cc`](https://github.com/pufereq/simulat/commit/ee340cc33442c7c994c8f4bc30e493e284443b47) **widget.py**: Add `Widget` class
- [`0ae0437`](https://github.com/pufereq/simulat/commit/0ae0437cea680fbb75c73b354881a9b5c85c3b16) **container.py**: Add `Container` class
- [`b58f6c8`](https://github.com/pufereq/simulat/commit/b58f6c80f83cb526cde608c4ce97bffe32652180) **window.py**: Modify title alignment (center > left)
- [`f1595a9`](https://github.com/pufereq/simulat/commit/f1595a916dd87e18ab9e7a72ec1f1d920b7610d9) **window.py**: Add `set_title()` method

### Miscellaneous Tasks

- [`4a707bf`](https://github.com/pufereq/simulat/commit/4a707bfa3369139af09d7dd30d58e77bd89f6b05) **release**: 0.5.0-alpha.1
- [`9b395d4`](https://github.com/pufereq/simulat/commit/9b395d42bc1f9f2d29e1c2f20345266497d39777) **release_it.yml**: Add release_it workflow
- [`429542d`](https://github.com/pufereq/simulat/commit/429542d4307eaf17f7a95cb26bef42a4188730da) **release_from_tag.yml**: Delete `release_from_tag.yml`
- [`d90e4dc`](https://github.com/pufereq/simulat/commit/d90e4dc227c01d93eb9bdb8c0904a3693ca5a9fa) **bump_version.yml**: Remove `bump_version.yml`
- [`16d6e31`](https://github.com/pufereq/simulat/commit/16d6e31aaf4ac5e6c8e7e1d6a6f387b4b985baf1) **.cz.toml**: Modify commitizen config to allow for pre-releases
- [`c166a6c`](https://github.com/pufereq/simulat/commit/c166a6c7e5bf6e10b5b5340f9e71321bb3e1a85a) **release_from_tag.yml**: Add release from tag workflow
- [`e2eb19c`](https://github.com/pufereq/simulat/commit/e2eb19c8384838deb0ee9821945dc49c9ac77458) **main.py**: Modify imports and calls from `test()` to `container_test()`
- [`f99a14e`](https://github.com/pufereq/simulat/commit/f99a14e0113ca304621740ff0dd818f04f8480e7) **container.py**: Modify `Container.loop()` to respect new timeout set in loop.py
- [`ec8473b`](https://github.com/pufereq/simulat/commit/ec8473bc74026fb0e9222c9ecf978cb005d1f418) **loop.py**: Split main loop from handler
- [`b11ec6c`](https://github.com/pufereq/simulat/commit/b11ec6cfe806a830b5921cfab9db7682c9810713) **game_loop**: Improve frame timing
- [`bbb3a71`](https://github.com/pufereq/simulat/commit/bbb3a7157c49c3ed1e0c39ede85762477b86023f) **map_layout.py**: Modify import and reference to point to `container_test()` function in container.py
- [`0d11156`](https://github.com/pufereq/simulat/commit/0d111564d65525a057d8590f9ad5d9a4506f4fd9) Move `test()` from main.py to `container_test()` in container.py
- [`d3428ea`](https://github.com/pufereq/simulat/commit/d3428eaeeb19d46a61cc074a64cfdd126fc103c5) **main.py**: Make main menu smaller
- [`a41e7a0`](https://github.com/pufereq/simulat/commit/a41e7a04d43f7d6f12f3609863fffd7379f0c3ea) **menu_widget.py**: Add return prompt to info display
- [`3a246c5`](https://github.com/pufereq/simulat/commit/3a246c5e5b840b95946d922e8ac36454beec4082) **menu_widget.py**: Modify entry label display in info view to increase UI readability
- [`1bbacb1`](https://github.com/pufereq/simulat/commit/1bbacb1a7d5f9307990160ca62c116a47a0f951f) **menu_widget.py**: Modify `display` method to center menu entries in container
- [`5110ab7`](https://github.com/pufereq/simulat/commit/5110ab7cb93b50c2a13e27511a39d28372999017) **container.py**: Move `content_win` import into `Container` class constuctor
- [`514e951`](https://github.com/pufereq/simulat/commit/514e9518bb95559a4e8cbc05908b5bef15566ee2) **menu_widget.py**: Reduce spacing between info title and info text
- [`92f48dc`](https://github.com/pufereq/simulat/commit/92f48dc98630966ea28d53c98086c8a186a98b8e) **main.py**: Modify `Container`'s `nlines` argument to make it bigger
- [`6680fb7`](https://github.com/pufereq/simulat/commit/6680fb7c46b376975d9b1b86f2667e5ccfdd4cdf) **main.py**: Add `description` argument in call to `Container`
- [`4221466`](https://github.com/pufereq/simulat/commit/422146665428895d84d2e90d8e45a709e0fc4cab) **widget.py**: Modify size and position of widget to make space for `Container`'s description
- [`4182086`](https://github.com/pufereq/simulat/commit/4182086328b744c1b4ed19cde061db1b39324a49) Add `.mailmap`
- [`54cf308`](https://github.com/pufereq/simulat/commit/54cf308ab13132d65cc448b349156969cf4ed2b2) **requirements.txt**: Remove unused dependecies
- [`9c01a40`](https://github.com/pufereq/simulat/commit/9c01a4082a461d2fadefb68f433a2355a4445b08) **.gitignore**: Add `env` folder to gitignore
- [`5cabae2`](https://github.com/pufereq/simulat/commit/5cabae29c1c018418f6888a806791feb3c8f4cf4) **bump_version.yml**: Auto releases are drafts for modifications to body

### Refactor

- [`7c56573`](https://github.com/pufereq/simulat/commit/7c56573532ffb3d78060d18b664859eb4b32a9ef) **main.py**: Modify `main_menu` to use `Container` and `MenuWidget` instead of old `Menu` class

### Styling

- [`941770d`](https://github.com/pufereq/simulat/commit/941770d024bef9c19c580849639188a8670d16d8) **container.py**: Move list comprehensions below for better readability
- [`cbd0283`](https://github.com/pufereq/simulat/commit/cbd02838ab9dee2997e07e4744723e49f307898f) **game_map.py**: Remove commented-out code

### Build

- [`bbdb04c`](https://github.com/pufereq/simulat/commit/bbdb04c930d224c9835c43a1ff98e540480260e4) **.release-it.toml**: Add `.release-it.toml`
- [`32c0c0b`](https://github.com/pufereq/simulat/commit/32c0c0b45280ca16d137462197ec33828f6c505c) **requirements.txt**: Add `requirements.txt`

## [0.4.0] - 2023-09-06

### Bug Fixes

- [`17c8c79`](https://github.com/pufereq/simulat/commit/17c8c7937e28f8fed98e5141ea1253fe86f423bc) **game_map.py**: Fix player moving when camera move called
- [`f94cfc1`](https://github.com/pufereq/simulat/commit/f94cfc1f64bb4e9734030a176722d291068e59a8) **game_map.py**: Fix door glitching when interacted while door's position = player's position
- [`fe32fc5`](https://github.com/pufereq/simulat/commit/fe32fc514c6a3624216ac457a867bd7308686cfd) **door.py**: Fix `__repr__()` not returning a string
- [`57f37ed`](https://github.com/pufereq/simulat/commit/57f37ed1d5560925aa04cd1728e41174ada0b9ba) **game_map.py**: Fix pad restricting map by being too small
- [`6d2338f`](https://github.com/pufereq/simulat/commit/6d2338ff64cb19c533ecc2ec1807da901c86effd) **game_map.py**: Fix typo in calculation of `self.max_displayed_pad_size` in `_resize()` method
- [`68d9980`](https://github.com/pufereq/simulat/commit/68d9980efd840c01bce5097e816857fe2c749134) **game_map.py**: Adjust `pad_view_left` and `pad_view_top` calculations
- [`6c92c30`](https://github.com/pufereq/simulat/commit/6c92c30cd3e03e5fb6a8a8e40667a7931e21ef59) **game_map.py**: Fix title not being displayed properly on topbar
- [`9faeef4`](https://github.com/pufereq/simulat/commit/9faeef4835f63778e9387ecfe699793291478dc1) **game_map.py**: Fix pad not spanning whole terminal
- [`57f3ac1`](https://github.com/pufereq/simulat/commit/57f3ac1b8d14efea1660ddb5c6d00878550bfab3) **game_map.py**: Fix player leaving behind a black box when moving first time
- [`51ea090`](https://github.com/pufereq/simulat/commit/51ea0904441ca0c3e321fcb4396a9a57e5a79627) **game_map.py**: Fix player not appearing when map loaded
- [`8370b48`](https://github.com/pufereq/simulat/commit/8370b4896b6e426fbaf297ef65d442cd810fc2ab) **init.py**: Fix AttributeError when calling content_win.panel
- [`a8994e3`](https://github.com/pufereq/simulat/commit/a8994e3552c4700bbaf23221d115caf775c87c60) **game_map.py**: Fix error when going out of negative bounds
- [`027bc3e`](https://github.com/pufereq/simulat/commit/027bc3e493bc8a53bc9c9efd0916e90467ea122b) **game_map.py**: Fix screen flicker when moving
- [`fd8defe`](https://github.com/pufereq/simulat/commit/fd8defec85db7a5bb968f7af16983e2b22422afb) **menu.py**: Fix menu disappearing when content_win.panel's window replaced

### Documentation

- [`6efb018`](https://github.com/pufereq/simulat/commit/6efb018d0126ba464f8368f8b3cf96a3f2329b62) **game_map.py**: Add missing comment

### Features

- [`83e5ab7`](https://github.com/pufereq/simulat/commit/83e5ab7e580a5416895c1cfdc2462a504dd7bc8b) **game_map.py**: Add camera controls
- [`cda006f`](https://github.com/pufereq/simulat/commit/cda006f9dd5d0f6624c03cfa4ac277484123d4e2) **game_map.py**: Modify `GameMap()` class to use cell classes
- [`0e6f26b`](https://github.com/pufereq/simulat/commit/0e6f26b1562770e5fdc65502c4c008d04a82a320) Add cell classes
- [`e054edb`](https://github.com/pufereq/simulat/commit/e054edbbc570f9af9d9106f6490d51847d17c4a7) **game_map.py**: Replace `INTERACTIONS` with `self.interactions` in `_interact()` to avoid possible conflict
- [`8f5a9e9`](https://github.com/pufereq/simulat/commit/8f5a9e9237daa14d9cc41311494d85a47994be13) **map_layout.py**: Add some doors to the map for showcase
- [`d4020be`](https://github.com/pufereq/simulat/commit/d4020be620908a5f6a63819e4946a6795b68be52) **map_layout.py**: Add functionality to `example_action()`
- [`5555d4d`](https://github.com/pufereq/simulat/commit/5555d4d5d1e3b1387ed5055d62416c8de472b68a) **game_map.py**: Modify behavior of interacting with interactions to be more intuitive
- [`0a76854`](https://github.com/pufereq/simulat/commit/0a76854d871f76c2761ddda5c143db9ab43e9a06) **init.py**: Change floor color to be more realistic
- [`ffb26fd`](https://github.com/pufereq/simulat/commit/ffb26fd43674c2b38d564cc0b175ee17827fe138) **init.py**: Add colors for door characters
- [`affd599`](https://github.com/pufereq/simulat/commit/affd5990e80245001d943382ce33722ea17f8f0d) **game_map.py**: Add door character `"d"` and `"D"` which use `Door()` class
- [`9e7d059`](https://github.com/pufereq/simulat/commit/9e7d059e60d1f8b7ad567e074f58eaf7911a41da) **door.py**: Add `Door()` class
- [`6a6f879`](https://github.com/pufereq/simulat/commit/6a6f8791882ba8d663f0434f5bc44861b845c0e0) **map_layout.py**: Add floor to building
- [`f6de40a`](https://github.com/pufereq/simulat/commit/f6de40afc3418d83d4b2d058e6b5df56b82b351d) **game_map.py**: Modify texture of floor to add knots and cracks
- [`baa344f`](https://github.com/pufereq/simulat/commit/baa344fd5eff9094b0cbdd28725c524d81bc4bdb) **game_map.py**: Modify `self.grass_chars` for more realism
- [`650b050`](https://github.com/pufereq/simulat/commit/650b050043d9d976048cfa1eaa043b4cc5e73dd6) **game_map.py**: Add coordinates to `topbar.details_win`
- [`9582b5a`](https://github.com/pufereq/simulat/commit/9582b5af90291da1674f3cf06d4d51c16c68d24d) **init.py**: Modify color of `GRASS_PAIR`
- [`33abc04`](https://github.com/pufereq/simulat/commit/33abc04a86fcc45fd9e9d06c3296149a33b7ea4f) **game_map.py**: Modify not specified cells to be grass in _map_init()
- [`24824cc`](https://github.com/pufereq/simulat/commit/24824cc93c715783ee1e483a0ef1dfc6625f5e8a) **game_map.py**: Improve grass rendering
- [`cec44b7`](https://github.com/pufereq/simulat/commit/cec44b7e68c34bbb3206fc1c35d4dacb2ff32050) **game_map.py**: Utilize color; add floor, grass char
- [`6c72948`](https://github.com/pufereq/simulat/commit/6c729486334ba859f9192dcf5300e433a7354682) **init.py**: Add color support
- [`9fb1a79`](https://github.com/pufereq/simulat/commit/9fb1a795b6e974288e2f0a4e0d64b3321e2d8e06) **game_map.py**: Modify _move_player() to restore the original character before moving the player
- [`9a7f5b0`](https://github.com/pufereq/simulat/commit/9a7f5b067c9110c865f6bb7c94227f785904a793) **game_map.py**: Change _draw_map() to set attribute of interactive chars to cs.A_REVERSE
- [`1ec687e`](https://github.com/pufereq/simulat/commit/1ec687e69136c1143c83fdf377303b91c2e40b28) **game_map.py**: Change interaction behavior
- [`5bec804`](https://github.com/pufereq/simulat/commit/5bec8044ebddbf587dcea3ea46a818da445104af) **loop.py**: Add game_map._refresh_map() call
- [`508e82d`](https://github.com/pufereq/simulat/commit/508e82d1f992c79c43a4433efa6c6d56068ecd3b) **loop.py**: Add terminal resize handling
- [`6cf55e3`](https://github.com/pufereq/simulat/commit/6cf55e3c544962dec89802247f201f0ebe65a05a) **game_map.py**: Add _resize method
- [`5397dae`](https://github.com/pufereq/simulat/commit/5397dae778c0d3ff396d9be95f6fe6cbb876fcf0) **loop.py**: Handle keypresses directly from loop and use new arguments in call to game_map._input()
- [`4aa48bf`](https://github.com/pufereq/simulat/commit/4aa48bf6ce0857c7aecec208b2ea2081221210f8) **game_map.py**: Add _refresh_map() method for future use
- [`8e2f084`](https://github.com/pufereq/simulat/commit/8e2f084f48b13a1ca59c58a5c1ff81db57559d29) **game_map.py**: Make _input() accept key presses as argument to work with game_loop()
- [`16d9786`](https://github.com/pufereq/simulat/commit/16d9786c0c8da4a2283a5c832db850e82780ddf0) **game_map.py**: Limit camera to not exceed positive map limit
- [`064499f`](https://github.com/pufereq/simulat/commit/064499fe73d634831aac69dbe0940a423f9f5db1) **main.py**: Modify main_menu() to call game map
- [`282c831`](https://github.com/pufereq/simulat/commit/282c8313c73d184a5e16b931885004458b06ed54) **init.py**: Add init_game_map()
- [`474cfd8`](https://github.com/pufereq/simulat/commit/474cfd8f82d6e4b3f9049ead1db53e3e91a1b73d) **loop.py**: Add game loop
- [`22b9139`](https://github.com/pufereq/simulat/commit/22b9139447e63119d8847f5c8aae505b4b1452bf) **map_layout.py**: Add map layout
- [`eaf95b4`](https://github.com/pufereq/simulat/commit/eaf95b4381643c467d58af845ed49e88245fac93) **game_map.py**: Add open world
- [`f01ea15`](https://github.com/pufereq/simulat/commit/f01ea154629f557a4288d15da4c7f060fc8dea64) **pad.py**: Add curses pad support
- [`a483978`](https://github.com/pufereq/simulat/commit/a483978a59044ef82487f5fe99a5db25c5c946db) **window.py**: Add *args and **kwargs for future pad management
- [`6039d19`](https://github.com/pufereq/simulat/commit/6039d19305ec4bb737dd550b15548a64dc9fb9cb) **window.py**: Remove refresh() calls from border() and addstr() for more classic behavior

### Miscellaneous Tasks

- [`7e155d4`](https://github.com/pufereq/simulat/commit/7e155d47ecea9a2266d8926ddd1038aa9953de6e) **game_map.py**: Remove unnecesarry imports
- [`578071a`](https://github.com/pufereq/simulat/commit/578071a35f0f26159781bebdc1c329174fc7ca61) **cell.py**: Remove unnecessary imports
- [`b630e60`](https://github.com/pufereq/simulat/commit/b630e604819c3ef444284f9846e33d7087f1e273) **door.py**: Remove obsolete door.py
- [`6997777`](https://github.com/pufereq/simulat/commit/69977777285d7b6cd10730924f0f7209c64715b5) **.cz.toml**: Add missing space

### Refactor

- [`f7b150e`](https://github.com/pufereq/simulat/commit/f7b150e5ca2784625c0d6d6026e1f720ce4ae0f4) Refactor curses initialization
- [`255bcc0`](https://github.com/pufereq/simulat/commit/255bcc02d1b8461b2419ef9380cdd2d4a689dd90) **game_map.py**: Change variable name
- [`d6db94e`](https://github.com/pufereq/simulat/commit/d6db94eab0866e81b29a3f5829667ecdec8927c8) **game_map.py**: Remove unnecessary additions in self.pad_size

### Styling

- [`fec5543`](https://github.com/pufereq/simulat/commit/fec55432580ed0d0ee5552ea5a82f086b3d1f40c) **game_map.py**: Split import of `*COLOR` from `simulat.core.init` for better readability
- [`59c64f5`](https://github.com/pufereq/simulat/commit/59c64f5a57c234062b200b9f6a5bfefbf41ebd21) **game_map.py**: Add inline comment at `self.MAP_SIZE` definition
- [`7d2cb14`](https://github.com/pufereq/simulat/commit/7d2cb14cefa98e85d6158cb6de0ef76f3a5cf5f4) **game_map.py**: Add comments
- [`826828c`](https://github.com/pufereq/simulat/commit/826828c9e5063f2ab0b595404391a5c41a25a530) **loop.py**: Add spacing before function definition
- [`cb5c956`](https://github.com/pufereq/simulat/commit/cb5c9562520c9536809020fb60aa9fc922174585) **game_map.py**: Remove commented code

## [0.3.0] - 2023-07-31

### Bug Fixes

- [`e018f85`](https://github.com/pufereq/simulat/commit/e018f851cf7e9fc7ee534b3035d8a511ee0d15d7) **menu.py**: Fix borders not appearing
- [`5ebe110`](https://github.com/pufereq/simulat/commit/5ebe110ff2a3fec7eabb2f1c05e7c305ceba675a) **error_handler.py**: Fix retrying not working correctly

### Features

- [`d896b04`](https://github.com/pufereq/simulat/commit/d896b0443d755bc01f528727046639640cbad609) **board.py**: Limit max movement speed
- [`fad8c00`](https://github.com/pufereq/simulat/commit/fad8c001cca42858e411c89eff36dda4854d630a) **init.py**: Make content_win not a panel
- [`757df41`](https://github.com/pufereq/simulat/commit/757df413aa41d2ef78aa8b49753e3510b9520c0c) **window.py**: Update calls to SubWindow and DerWindow to include named args
- [`1b15cf2`](https://github.com/pufereq/simulat/commit/1b15cf2d8f1b864593f59d436f9a689e58df433b) **window.py**: Make make_panel and reverse named arguments
- [`7a009d1`](https://github.com/pufereq/simulat/commit/7a009d17e3e826f46dd42553be04ff8e3f6cb0f2) **derwindow.py**: Make make_panel and reverse named arguments
- [`06bdd65`](https://github.com/pufereq/simulat/commit/06bdd6513895f2bc481e658dec8adc0a81e7b688) **subwindow.py**: Make make_panel and reverse named arguments
- [`ce6b8bd`](https://github.com/pufereq/simulat/commit/ce6b8bd6a55657b823776319a6d67b5c91d132a8) **subwindow.py**: Move addstr() and cs_addstr() to window.py
- [`2da110b`](https://github.com/pufereq/simulat/commit/2da110be70760fc76b9ae35943ded50cfd98bde9) **error_handler.py**: Make full_path cleaner
- [`6390750`](https://github.com/pufereq/simulat/commit/6390750584804710ede6bfb12897fa68cf2fbe1f) **main.py**: Use error_handler on main_menu()
- [`42e9379`](https://github.com/pufereq/simulat/commit/42e93798e0f7b083848149096c5b6a4443359f2f) **error_handler.py**: Make exception menu description more concise
- [`ccb9113`](https://github.com/pufereq/simulat/commit/ccb9113dd04ac5ab23f645ff92e10cadfbeae6b7) **error_handler.py**: Add retry option for caught exceptions
- [`3f3a9d8`](https://github.com/pufereq/simulat/commit/3f3a9d8ba424636890820caa737d04b618ca283f) **derwindow.py**: Add DerWindow class
- [`01e0d15`](https://github.com/pufereq/simulat/commit/01e0d15861ab660e16092fa3ca29b331107342ba) **subwindow.py**: Use _common_init() inherited from Window()
- [`b9a2c16`](https://github.com/pufereq/simulat/commit/b9a2c1666083b06c5e10145c602288d5cd0b863d) **window.py**: Add _common_init() to remove duplicate code

### Miscellaneous Tasks

- [`f37004b`](https://github.com/pufereq/simulat/commit/f37004bfb83bd6cdb600b1d760f82dbb85110061) **topbar.py**: Include named args in call to Window()'s init
- [`797dee5`](https://github.com/pufereq/simulat/commit/797dee59ac268f33ab7af814fc4d3b8b7b36ff75) **menu.py**: Include make_panel argument in player_window and board_window
- [`e95b3a4`](https://github.com/pufereq/simulat/commit/e95b3a47e886823bdfe9e06e4bb22677197a0a9d) **menu.py**: Change parent of description_window
- [`d581521`](https://github.com/pufereq/simulat/commit/d58152154fc7dcdee9882d164255580675560759) **menu.py**: Include make_panel argument in description_window and info_window
- [`378bc10`](https://github.com/pufereq/simulat/commit/378bc101aeced4ac9b5c5901eb25b84fb5ed4ce6) **.cz.toml**: Add bump_message config

### Refactor

- [`80844e3`](https://github.com/pufereq/simulat/commit/80844e3699576d6496c824258ee96d18efcbc178) **menu.py**: Implement window management on info_window and info_window_border
- [`9630814`](https://github.com/pufereq/simulat/commit/9630814d18284375e9d5c6dd207fdc475795c062) **menu.py**: Make description_window_border and description_window DerWindows
- [`8f515f5`](https://github.com/pufereq/simulat/commit/8f515f55ac1e31a1cd98967bcf79d58ae34bae8d) **menu.py**: Make root_window and root_window_border Windows instead of SubWindows
- [`00d7f01`](https://github.com/pufereq/simulat/commit/00d7f01b028f94c45d980ca1e56bf1f3bdbe3bcf) **menu.py**: Remove unused code
- [`89441af`](https://github.com/pufereq/simulat/commit/89441afb134213967c36632c1f0b83d1853a697e) **menu.py**: Use f-string padding for label formatting

### Styling

- [`2897355`](https://github.com/pufereq/simulat/commit/28973554b37d71bf1a16ca62325e5f547ebf59ad) **bump_version.yml**: Remove trailing whitespace

## [0.2.0] - 2023-06-22

### Bug Fixes

- [`0444637`](https://github.com/pufereq/simulat/commit/04446374bc386f8d62cd8d84bfe91c2c029b166e) **bump_version.yml**: Use new token
- [`6e48aaa`](https://github.com/pufereq/simulat/commit/6e48aaa93f1a1f1ee9268e8bfde38cb20fc09f3f) **bump_version.yml**: Add permission bypass to omit branch protection
- [`90c6508`](https://github.com/pufereq/simulat/commit/90c650807b8b805a3a0473c89104bd973397fe4d) **bump_version.yml**: Change token back to default
- [`7ded37b`](https://github.com/pufereq/simulat/commit/7ded37b22611d4308040a71cf654e52cedc56bc7) **bump_version.yml**: Fix permission denied when creating tag
- [`c1ea05d`](https://github.com/pufereq/simulat/commit/c1ea05dda44a7f308bc8b6083ff4d40ccc051fca) **bump_version.yml**: Omit error when signing tag
- [`5800675`](https://github.com/pufereq/simulat/commit/5800675099f78f62e42a4004ec18d8ff9272dc1b) **subwindow.py**: Fix error when using addstr() in a nested subwindow
- [`fec6a6a`](https://github.com/pufereq/simulat/commit/fec6a6a0a22548169b12693c7dbd2cdb403ae327) **subwindow.py**: Fix error when nesting subwindows
- [`c770c2c`](https://github.com/pufereq/simulat/commit/c770c2c6a5ddb8370b3f15a82034e8fe85233ff7) **window.py**: Variable name typo

### Documentation

- [`f9abb3c`](https://github.com/pufereq/simulat/commit/f9abb3c8c712f9bdf652db1c421fe398c24ee229) **PULL_REQUEST_TEMPLATE.md**: Add PR template
- [`7e2d41c`](https://github.com/pufereq/simulat/commit/7e2d41c66c6c65eed1cdc96e41f968a6f4e72967) **CHANGELOG.md**: Rewrite changelog
- [`37822cf`](https://github.com/pufereq/simulat/commit/37822cfd1bf650e230edbf29d666948ddfdc70b5) **board.py**: Remove typo in docstring
- [`ecfa564`](https://github.com/pufereq/simulat/commit/ecfa56498f9d32a618b7981ab540cd420652b4a4) **README.md**: Correct wakatime link
- [`bd6d8b9`](https://github.com/pufereq/simulat/commit/bd6d8b9204956b09546c0b32ae9c7738a871474a) **README.md**: Add wakatime stats

### Features

- [`367c10d`](https://github.com/pufereq/simulat/commit/367c10dd32ff531efcea96b2205055bdb508c4cd) **board.py**: Add error_handler decorators
- [`304708c`](https://github.com/pufereq/simulat/commit/304708c2ef46f36e380ad7dcf111436ce8defb59) **main.py**: Add error_handler decorator back
- [`14a316a`](https://github.com/pufereq/simulat/commit/14a316ac6254347951d4fd8668b882598f1be658) **.cz.toml**: Remove gpg_sign
- [`9b2dc18`](https://github.com/pufereq/simulat/commit/9b2dc180449bf36ddcb76425635ae9d6f20ad043) **bump_version.yml**: Comment out gpg key import
- [`0e1fa17`](https://github.com/pufereq/simulat/commit/0e1fa17d6baf441a46209c1a7699ea934646083a) **board.py**: Implement window management
- [`723fc19`](https://github.com/pufereq/simulat/commit/723fc195e4f4d06cd53b1b08530764b8b7117f00) **window.py**: Add insch() method
- [`c636ec6`](https://github.com/pufereq/simulat/commit/c636ec69b8a8249e3e69cbe9af4e5c271bc1d6e5) **menu.py**: Implement window management
- [`a34fd87`](https://github.com/pufereq/simulat/commit/a34fd87970640e0d8e4a10cfe24a7c947e41e9aa) **subwindow.py**: Add cs_addstr method
- [`32e8c82`](https://github.com/pufereq/simulat/commit/32e8c8252cc22d4640ea1e5e10cc4931146452be) **init.py**: Implement window management
- [`1c6eb78`](https://github.com/pufereq/simulat/commit/1c6eb78fbdfaa21be182f2f1c603159f84fbb3de) **window.py**: Add curses methods to Window via encapsulation
- [`71d0ec8`](https://github.com/pufereq/simulat/commit/71d0ec8ff14cdae93fca7c91e855851110ab6cb1) **window.py**: Add curses.panel support
- [`6dc8cf9`](https://github.com/pufereq/simulat/commit/6dc8cf9588d32525840c9cbaf07f57708a5f7436) **subwindow.py**: Add curses.panel support
- [`3f77f5e`](https://github.com/pufereq/simulat/commit/3f77f5e73614ce68d68eb9ee73f30dff72c4fcbc) **board.py**: Update topbar call to match new implementation
- [`874ba37`](https://github.com/pufereq/simulat/commit/874ba37b5420d1b7e330cf5e0c0673c44b924c14) **main.py**: Update topbar call to match new implementation
- [`30588d2`](https://github.com/pufereq/simulat/commit/30588d23bd4054ef3ef3cd07b590be93aba04e29) **window.py**: Add support for curses atrributes in whole window
- [`8f20599`](https://github.com/pufereq/simulat/commit/8f205992bcb2c96802e58dc3dc93e458caf731d9) **topbar.py**: Implement window management
- [`b2773b8`](https://github.com/pufereq/simulat/commit/b2773b8d0ac5aa8edc0187a8078ad3e76ecdc277) **subwindow.py**: Add right alignment of text
- [`df3ce73`](https://github.com/pufereq/simulat/commit/df3ce73353bd2a8c4e4da30eb0eb443d34581b03) Add window management
- [`9e16302`](https://github.com/pufereq/simulat/commit/9e163029f6d3693038b95a155fec9f3d0ec03a42) **board.py**: Add curses.beep when interacted with a collider
- [`46bb23e`](https://github.com/pufereq/simulat/commit/46bb23e89418d818a414405a2a16316da5ec2624) **board.py**: Add support for displaying board title on topbar

### Miscellaneous Tasks

- [`1adc6a0`](https://github.com/pufereq/simulat/commit/1adc6a0c2d7d8bcaa999bd01b0224600a20485c5) **bump_version.yml**: Run job if executed manually
- [`4b362f8`](https://github.com/pufereq/simulat/commit/4b362f845241065d39ec76d15c1b3e32b8de68a6) **bump_version.yml**: Add manual execution
- [`49226e5`](https://github.com/pufereq/simulat/commit/49226e516d26b2c1e18ecddb847dd79b9949709b) **bump_version.yml**: Add push argument to commitizen
- [`3fb1f69`](https://github.com/pufereq/simulat/commit/3fb1f69763dcba0a36b49f4b522f15574de759f5) **.gitignore**: Remove .simulat_old
- [`42ff481`](https://github.com/pufereq/simulat/commit/42ff4815695b24464ec280e3ec3de80af0ec5f4e) **bump_version.yml**: Change job to run only if 'gh-release' present
- [`f0b564c`](https://github.com/pufereq/simulat/commit/f0b564cc4edc07035b9331e486cccce8fc672c82) **actions/bump_version.yml**: Add gpg signing of bump commit
- [`e786785`](https://github.com/pufereq/simulat/commit/e786785e733eb779a887a8af11f23941a4382f4a) **actions/bump_version.yml**: Auto release after bump
- [`3ffcf5d`](https://github.com/pufereq/simulat/commit/3ffcf5d965106228117ca00c73dd5bc8efcf0bba) **actions**: Add commit_check.yml
- [`c672e28`](https://github.com/pufereq/simulat/commit/c672e2892602c3e4d18d35ac41ca7519c5d33df5) Add .github/workflows/bump_version.yml
- [`017ef02`](https://github.com/pufereq/simulat/commit/017ef020624b1f2f13dd2a78fd6f928b0fb56218) **.cz.toml**: Add gpg_sign and annotated_tag to commitizen config
- [`8ae0247`](https://github.com/pufereq/simulat/commit/8ae0247804c3bde1cde100573206f6e2271dc980) Add commitizen pre-config hook
- [`16678eb`](https://github.com/pufereq/simulat/commit/16678eba8074fd1158c9d061f553eca0fe2064e7) Add __init__.py

### Refactor

- [`dc57c9d`](https://github.com/pufereq/simulat/commit/dc57c9da9f4702953b5dd04605863dde04a28934) **.cz.toml**: Remove commented code
- [`4b6647c`](https://github.com/pufereq/simulat/commit/4b6647c45886e28d79a294958d489d61a8a05b1d) **window.py**: Remove unnecesarry blank lines
- [`a820d55`](https://github.com/pufereq/simulat/commit/a820d55e14369f89cd5ef95a2affd4b1fbac8e56) **window.py**: Fix whitespace in function definitions
- [`d3d4473`](https://github.com/pufereq/simulat/commit/d3d447332b73efe346866fe65c08e90f5c0db97a) **topbar.py**: [**breaking**] Remove obsolete clear* and update* functions
- [`13ca4c1`](https://github.com/pufereq/simulat/commit/13ca4c133ad18cef7ccbd0e09ad8d3b87b1d91f1) [**breaking**] Move simulat/core/windows to simulat/core/ui/windows

### Bump

- [`13f916f`](https://github.com/pufereq/simulat/commit/13f916fd8d6c2c285800827d14a499e79ea541fb) Version 0.1.0 → 0.2.0

## [0.1.0] - 2023-04-15

### Bug Fixes

- [`6bef999`](https://github.com/pufereq/simulat/commit/6bef999f9c03c11b20ff343158e15cb710cf6611) **board.py**: Fix error when only one of 'args' and 'kwargs' provided
- [`4065498`](https://github.com/pufereq/simulat/commit/40654985f1a25224e2232d192c4abeac9b102245) **menu.py**: Fix error when only one of 'args', 'kwargs' provided
- [`1145df9`](https://github.com/pufereq/simulat/commit/1145df9d3da7974e42ac06f690832b9cf9f6cf0f) **menu.py**: Fix button padding
- [`a9a6e4e`](https://github.com/pufereq/simulat/commit/a9a6e4e93faef457ac2ad262301d51996c9b194c) **menu.py**: Fix error when centered = True
- [`4e211e6`](https://github.com/pufereq/simulat/commit/4e211e6062ab1da6cc28a1aa6bdf2993aa3b4278) **board.py**: Fix arrow keys not working
- [`ec85c29`](https://github.com/pufereq/simulat/commit/ec85c29c33c22979f5eb8ac27da9581a48045b78) **board.py**: Fix '@' character visible in corner

### Documentation

- [`4fafdbe`](https://github.com/pufereq/simulat/commit/4fafdbe9b850791a2e3d712ebebef047fca81559) **board.py**: Update docstrings
- [`be92780`](https://github.com/pufereq/simulat/commit/be92780afeac1425d37b0bc30240b54482c8bf4c) **board.py**: Add docstrings

### Features

- [`d555c17`](https://github.com/pufereq/simulat/commit/d555c17a065a95235d8af2f084bbbad956b12cd9) **example.py**: Add Board() examples
- [`6a09a5f`](https://github.com/pufereq/simulat/commit/6a09a5fa3439e8d3e0a8990313852cda8f4bd3f8) **main.py**: Add label to 'board' item in main menu
- [`3d59ce9`](https://github.com/pufereq/simulat/commit/3d59ce9aa662ada4e1fa86d3313532661793cf65) **main.py**: Change 'board' target to display example board
- [`bd13025`](https://github.com/pufereq/simulat/commit/bd13025addcf7186acf94e708bd115ad748852d6) **board.py**: Add title rendering
- [`6e657d3`](https://github.com/pufereq/simulat/commit/6e657d3a1130c7b638e92fb775f96d15e121c147) **menu.py**: Add support for both args and kwargs in one target
- [`f25823e`](https://github.com/pufereq/simulat/commit/f25823e4c6a712c3fe26180b14986eb0288bcc57) **board.py**: Add support for doors
- [`5d280f9`](https://github.com/pufereq/simulat/commit/5d280f9d888ae2b9690b81e45e70708efffec0c0) **board.py**: Extend door characters
- [`580ae70`](https://github.com/pufereq/simulat/commit/580ae70ce8ecb5de4ad554f0781dd92ad47566ef) **__init__.py**: Add __init__.py
- [`2a1722d`](https://github.com/pufereq/simulat/commit/2a1722d9278a1a0beda1329c7244c13a53a59fe6) **main.py**: Add board item to main menu for debigging purposes
- [`e406cfc`](https://github.com/pufereq/simulat/commit/e406cfc5c783eddc21e1b00112c3b8a68f23ee77) **board.py**: Add support for custom board actions
- [`856103d`](https://github.com/pufereq/simulat/commit/856103df36f70f40794ba74e4121e8316006d6f2) **board.py**: Add board manager

### Miscellaneous Tasks

- [`70622f9`](https://github.com/pufereq/simulat/commit/70622f90c335ca7754469356d020281d0c8bf2b2) Version bump

### Refactor

- [`a195fc3`](https://github.com/pufereq/simulat/commit/a195fc387b3527853df883ed66bea4cf57e6e8aa) **board.py**: Remove unnecesarry import and unused variable
- [`3e91e27`](https://github.com/pufereq/simulat/commit/3e91e279b3085dde5b8cd986a6d4a33be2a38f75) Remove debug function
- [`c15cff1`](https://github.com/pufereq/simulat/commit/c15cff1e392878e33b244bb006d694dcd9d0bbab) **board.py**: Change variable name board_str -> board_layout

### Styling

- [`f53a030`](https://github.com/pufereq/simulat/commit/f53a030d6b750b71ed85183074bcb3ab551f36d7) **board.py**: Remove commented out code
- [`5bcf12f`](https://github.com/pufereq/simulat/commit/5bcf12f207b1a9690c1d783849e057ea826c9175) **board.py**: Change variable names to meet style requirements

## [0.1.0-dev.2] - 2023-03-31

### Documentation

- [`66057b0`](https://github.com/pufereq/simulat/commit/66057b038b0b3d51b8ca5a595c675ddd7be16e9c) **changelog**: Add CHANGELOG.md
- [`9c5d902`](https://github.com/pufereq/simulat/commit/9c5d902bc895244ebf35c2f54890bbf1b2aedcf8) **readme**: Add CodeFactor badge for develop branch

### Features

- [`2149ca4`](https://github.com/pufereq/simulat/commit/2149ca45ba3c2339506ee3adc1df53541a54fe99) **main.py**: Remove debug code
- [`739ca8a`](https://github.com/pufereq/simulat/commit/739ca8a18d07fc594cffaa7eb33ddab76931ab12) **menu.py**: Correct info window position
- [`9ea323a`](https://github.com/pufereq/simulat/commit/9ea323a28bb3ac455e619dc498ce0d4a66964b25) **menu.py**: Correct button spacing and remove unnecessary code
- [`c0efd81`](https://github.com/pufereq/simulat/commit/c0efd812c48e8ba7818ac4044152a2dc29aab6cf) **menu.py**: Update menu layout and info window width calculation to center properly
- [`9fd53e3`](https://github.com/pufereq/simulat/commit/9fd53e3d4d015f80f38f0ee9e399246fbe6b9b9c) Add 'raise an  exception' button
- [`2190b61`](https://github.com/pufereq/simulat/commit/2190b6171c8843843d8d88875b84b4b98e4d237a) **core**: Add error handler
- [`3aa87a7`](https://github.com/pufereq/simulat/commit/3aa87a7ad13b805c89274f5873d33e3c0a2eac44) **ui**: Add support for newlines in menu handler
- [`c2ca936`](https://github.com/pufereq/simulat/commit/c2ca936aa584038f16cab981e027435d3deaaca4) **ui**: Clear menu windows upon cleanup
- [`83ff785`](https://github.com/pufereq/simulat/commit/83ff785678e628693bacc35480e77ca8e5f6f7ad) **ui**: Widened menu from 40 to 50 characters
- [`62c69be`](https://github.com/pufereq/simulat/commit/62c69be92d912fea0e44dce49410d02d7ee02857) Add exit option in main menu
- [`de5c54a`](https://github.com/pufereq/simulat/commit/de5c54ade7dc8f9acab8aec8d752567e56c82b12) **ui**: Add ability to describe buttons in menu handler
- [`e34302d`](https://github.com/pufereq/simulat/commit/e34302db8b882c5359bc33bcb75d9e083ac2ae69) **view**: Add menu support for main menu
- [`ecc34b2`](https://github.com/pufereq/simulat/commit/ecc34b22acfc910460721a384d32e598927944fa) **ui**: Add menu handler

### Miscellaneous Tasks

- [`6b2bff8`](https://github.com/pufereq/simulat/commit/6b2bff8f1901973303b7a5719384da0de85f8960) **CHANGELOG.md**: Bump version
- [`aa443a5`](https://github.com/pufereq/simulat/commit/aa443a5f841e98413bc8412a534098e76f36455d) Implement error handler
- [`63b0fb4`](https://github.com/pufereq/simulat/commit/63b0fb4f15f3e94150cd340c820dc0172379bf6a) **init**: Change init order
- [`e546a77`](https://github.com/pufereq/simulat/commit/e546a77b0b5c9cc3bc5d9ea6b164de57b5348d9b) Implement `info` key to main menu

### Refactor

- [`a6ad9fc`](https://github.com/pufereq/simulat/commit/a6ad9fc42a457f459241a176820b9ce3ea55d7d1) Remove need for using keys when not needed in menu handler

### Styling

- [`9caaed3`](https://github.com/pufereq/simulat/commit/9caaed35bf49000ab519dfc289e8f6665f2fbdf2) **menu.py**: Add types to variable names to improve readability
- [`a23e9bc`](https://github.com/pufereq/simulat/commit/a23e9bc19131d29dce116d1ba92f2e78ac8e72f3) Clean up leftover comments and make code more readable

## [0.1.0-dev.1] - 2023-03-17

### Documentation

- [`a728fd8`](https://github.com/pufereq/simulat/commit/a728fd8d509d95022236777c8f8da68d3bd7d6ac) Add .gitignore
- [`e666deb`](https://github.com/pufereq/simulat/commit/e666debdb4cffd3c0df509a7b440af57b1880280) Add CODE_OF_CONDUCT.md
- [`53394a0`](https://github.com/pufereq/simulat/commit/53394a014fd0c4afe8c0092051a5daf373cd2882) Add CONTRIBUTING.md
- [`dd27dfc`](https://github.com/pufereq/simulat/commit/dd27dfcaa6bc63a742756523f0e28518ad600aee) **readme**: Add README.md
- [`fc64e79`](https://github.com/pufereq/simulat/commit/fc64e79918d00b151abc9c8f39b418b5ec88f55f) Add LICENSE

### Features

- [`eb52767`](https://github.com/pufereq/simulat/commit/eb5276777f6e421ccfde24a676c0f73aabb5be15) Add main.py
- [`0ca7379`](https://github.com/pufereq/simulat/commit/0ca73798c25f30a15eeaf6bbb1165d0e60fb2fe1) **init**: Add init.py
- [`7126eef`](https://github.com/pufereq/simulat/commit/7126eef170c92c7a253dded1359f5aad6d16f8d6) **ui**: Add topbar

### Build

- [`11cd1e4`](https://github.com/pufereq/simulat/commit/11cd1e4cbc7e1655d6b4739620f8206d7c473c86) Add .vscode

<!-- generated by git-cliff -->

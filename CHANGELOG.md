# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0] - 2023-12-30

### Bug Fixes

- [`f40428e`](https://github.com/pufereq/simulat/commit/f40428ec6b04dea599a77ef12676ce2c16f75ff2) **loop.py**: fix windows resizing incorrectly
- [`c364b47`](https://github.com/pufereq/simulat/commit/c364b4799568360028a494487de390ec2dd47d4e) **loop.py**: fix error when screen resized below required size

### Features

- [`a9af2d7`](https://github.com/pufereq/simulat/commit/a9af2d7d72bf69a9491a3f7a420555bb4a4e9d79) **init.py**: add wrapper window

### Miscellaneous Tasks

- [`c3de0a6`](https://github.com/pufereq/simulat/commit/c3de0a6d5cbe5e059248b4350c13376b165bbdde) **main.py**: remove unnecessary arguments from `main_menu()`
- [`79c48a7`](https://github.com/pufereq/simulat/commit/79c48a778f20e0d9cd3b061558b15f01ae455e3b) **loop.py**: resize and redraw topbar on screen resize
- [`1cf1aff`](https://github.com/pufereq/simulat/commit/1cf1aff1e6e5195e579c6289773840394cbfce18) **init.py**: add `init_topbar()` method for topbar initialization
- [`235e372`](https://github.com/pufereq/simulat/commit/235e372294eba5d199cca5b890967b2199e4a1c0) **game_map.py**: modify `max_displayed_pad_size` set pad size using `wrapper_win` window
- [`0d3e267`](https://github.com/pufereq/simulat/commit/0d3e267991ce7de52bffed8befa7fe13b283612b) **container.py**: modify `move()` to center against `wrapper_win`
- [`383f930`](https://github.com/pufereq/simulat/commit/383f9306aabbe55bd1f449dbc95b74fba868b864) **topbar.py**: make topbar a derwin of `wrapper_win`

### Refactor

- [`9eb617b`](https://github.com/pufereq/simulat/commit/9eb617b5f6b29aa24d4280b20e4c4efe8550fc00) **game_map.py**: modify `topbar` calls to match rewrite
- [`4866888`](https://github.com/pufereq/simulat/commit/48668882443c60cd5ba44b950be4e9c577f4bd74) **main.py**: modify `topbar` calls to match rewrite
- [`83b5bde`](https://github.com/pufereq/simulat/commit/83b5bdea829d0c7f0a2d6c3ba8577509a31686e9) **topbar.py**: rewrite topbar

## [0.6.1] - 2023-12-20

### Bug Fixes

- [`6c5fd55`](https://github.com/pufereq/simulat/commit/6c5fd55683d56911b3628b67fa14f44d52c47150) **container.py**: fix menus not disappearing after loop finish

### Miscellaneous Tasks

- [`d6f5bc6`](https://github.com/pufereq/simulat/commit/d6f5bc6531e957bc26dd417afe9c14ba6cb53206) **release**: 0.6.1

## [0.6.0] - 2023-12-17

### Bug Fixes

- [`682457a`](https://github.com/pufereq/simulat/commit/682457a6c8d40aefad41a9adfc88169bec49831c) **console.py**: fix error when exiting console with `q` key
- [`43571fe`](https://github.com/pufereq/simulat/commit/43571fe1111566803ec356422b180903000c02e3) **console.py**: fix result always being `None`
- [`6260735`](https://github.com/pufereq/simulat/commit/62607357dfe1114d4a3f14ee7ec33395b7997014) **text_input_widget.py**: fix `default_text` not being written to the input field
- [`ef77d51`](https://github.com/pufereq/simulat/commit/ef77d5115a09cb02e8c0694b3a7083082297a33d) **text_input_widget.py**: fix text being overwritten on insert

### Features

- [`8020b3f`](https://github.com/pufereq/simulat/commit/8020b3f633163731a466c3307cc24745202750ee) **console.py**: add Console
- [`a0eb85e`](https://github.com/pufereq/simulat/commit/a0eb85ec0fc740cbbacfa08a34a22134e203c2cb) **widget.py**: make widgets panels and hide after init
- [`49a3873`](https://github.com/pufereq/simulat/commit/49a3873b9246b7cef118d490feedba1e9165d7fe) **container.py**: make containers' panel hidden after init

### Miscellaneous Tasks

- [`05f83c5`](https://github.com/pufereq/simulat/commit/05f83c5e1237d2d687422cfe89bc813be124eb9a) **release**: 0.6.0
- [`640fe97`](https://github.com/pufereq/simulat/commit/640fe97f91a1855a2093eb8a8b4ff6aba2783a86) **loop.py**: show console after pressing ` [backtick]
- [`f0af471`](https://github.com/pufereq/simulat/commit/f0af471d347b9ee8cf0890ff059fb85f8d1d11a7) **init.py**: add `Console` init function
- [`a0390b1`](https://github.com/pufereq/simulat/commit/a0390b119b8edb4e0eeead32cfbe6e1d19e5fb44) **text_input_widget.py**: move `cs.curs_set` call into the new `loop_start_hook()` method
- [`1bae156`](https://github.com/pufereq/simulat/commit/1bae15633706c5eab2aa90fde710f6a466b95b41) **container.py**: add call to `widget.loop_start_hook()`

### Refactor

- [`a765780`](https://github.com/pufereq/simulat/commit/a76578049de71aec540979878a8f5fd5b6a6b7f0) **window.py**: remove unnecessary type checking in `_common_init()`

## [0.5.0] - 2023-12-03

### Bug Fixes

- [`71028ab`](https://github.com/pufereq/simulat/commit/71028abc86764b79b70e6a80366e193e7c0850f8) **container.py**: fix error when `title` or `description` is not of type `str`

### Documentation

- [`7571ed7`](https://github.com/pufereq/simulat/commit/7571ed7f642991685ab845e4818a473324f8aff3) **CHANGELOG.md**: modify changelog to make commit messages lowercase

### Features

- [`1d24a89`](https://github.com/pufereq/simulat/commit/1d24a89c7a568e662d2d67fb5057acdb6d7b7ab5) **menu_widget.py**: add `get_toggle_entries` method to `MenuWidget`
- [`de8fc1f`](https://github.com/pufereq/simulat/commit/de8fc1f1ecc654a957c3b1a636c250e618350fa8) **meni_widget.py**: add help screen triggered by `?` key
- [`64f9760`](https://github.com/pufereq/simulat/commit/64f976052a5f4f66b199ce92faa6c26c1cafa8e2) **menu_widget.py**: add toggleable entries (`ToggleEntry`)
- [`7a4c318`](https://github.com/pufereq/simulat/commit/7a4c3182672df2c5760ebd8ed18b94776e146734) **menu_widget.py**: add `_display_notification` method

### Miscellaneous Tasks

- [`704a66a`](https://github.com/pufereq/simulat/commit/704a66a6f8e5eece728d52bdf66d7b0ff8b696ba) **release**: 0.5.0
- [`a75ae4d`](https://github.com/pufereq/simulat/commit/a75ae4d39a6d16479c6fc7f42ea29abae452de42) **menu_widget_tests.py**: add test for `[MenuWidget].get_toggle_entries()` method
- [`3544515`](https://github.com/pufereq/simulat/commit/35445150c4fea0b25930fe3982588a6759fd44df) **menu_widget.py**: set default_value of `ToggleEntry` as bool
- [`de82f6d`](https://github.com/pufereq/simulat/commit/de82f6da6a620f80457fa9e10915af4387327d26) **menu_widget.py**: add title to help menu
- [`5877b1c`](https://github.com/pufereq/simulat/commit/5877b1c2b3c8df053c410ba9edbf49b630ff7f3c) **menu_widget.py**: add `i` hotkey to help menu
- [`ebd53ab`](https://github.com/pufereq/simulat/commit/ebd53abfa90ca75e99c6234099f41916c7eb7a37) **main.py**: add menu entries for menu widget tests
- [`456899d`](https://github.com/pufereq/simulat/commit/456899d0175c3dadae7b8bf07193036d8b35263a) **menu_widget.py**: replace obsolete call to `_display_info` with `_display_notification`
- [`da32268`](https://github.com/pufereq/simulat/commit/da3226852135672fe9a840ab8aa8bc545a661927) **cliff.toml**: modify template to make all letters of commit message lowercase

### Refactor

- [`d9208c9`](https://github.com/pufereq/simulat/commit/d9208c9e3f99bf5c7c8fa1ec5218f1df1ecb005d) **menu_widget.py**: split `_input()` method into smaller methods
- [`214af10`](https://github.com/pufereq/simulat/commit/214af109aaeec218eb3d6ed5a643e2199f6ef1a9) **menu_widget.py**: improve help menu formatting

### Styling

- [`9e6decb`](https://github.com/pufereq/simulat/commit/9e6decb0e9956459c0c3a76918a6a9b79d01b549) **menu_widget.py**: add comments describing keybindings for better readability

### Testing

- [`20a6c84`](https://github.com/pufereq/simulat/commit/20a6c84b4bc291dbacd012c6326da3d2734c84c7) **menu_widget_tests.py**: add tests for menu widget

### Build

- [`da90e90`](https://github.com/pufereq/simulat/commit/da90e90f60397dc359e68e9e10bf2e3978898c87) remove `.pre-commit-config.yaml`

## [0.5.0-alpha.3] - 2023-10-29

### Documentation

- [`eea54ee`](https://github.com/pufereq/simulat/commit/eea54eef4be70fcf6ce12ff0aa1216f3d71983b6) **menu_widget.py**: remove Args section from class docstring

### Features

- [`dcc184b`](https://github.com/pufereq/simulat/commit/dcc184b2583061d5158318e5c8a47c42f917d8bc) **menu_widget.py**: add `locked_msg` argument and display it when selecting a locked entry

### Miscellaneous Tasks

- [`5319d98`](https://github.com/pufereq/simulat/commit/5319d98d480c9d2576d8e9d423254fc0259dec27) **release**: 0.5.0-alpha.3
- [`06ad077`](https://github.com/pufereq/simulat/commit/06ad077bc4385cae5e082948b668e16dfa8a9ec3) **release_it.yml**: update release_it workflow to use git-cliff
- [`167fe61`](https://github.com/pufereq/simulat/commit/167fe612aa6d956c9e812cd05f78ea066e5c9200) **.release-it.toml**: modify calls to now point to git-cliff
- [`b8b72e6`](https://github.com/pufereq/simulat/commit/b8b72e6538bcdc5c4eae4e1515b859805ce81879) **cliff.toml**: add git-cliff configuration file `cliff.toml`
- [`3f0533f`](https://github.com/pufereq/simulat/commit/3f0533f24acf924f238ae50f8e3a2339230fd150) **.cz.toml**: remove `.cz.toml`
- [`b1cab52`](https://github.com/pufereq/simulat/commit/b1cab521ca68fc0756b49cdab5d14d66e7d2f821) **menu_widget.py**: make new game `MenuEntry` locked
- [`9abef55`](https://github.com/pufereq/simulat/commit/9abef55e5f9bc88966f44871c886262aee04530c) **widget.py**: adjust widget size based on parent's `description` variable
- [`eeba2fa`](https://github.com/pufereq/simulat/commit/eeba2fa4ab575f738e03dc46f1527125105f6e2e) **container.py**: set description to an empty string if None instead of `No description provided.`
- [`57e9daf`](https://github.com/pufereq/simulat/commit/57e9daf42741edf2a869b15f4258a102f0490b76) **menu_widget.py**: disable confirming locked entries
- [`20ec781`](https://github.com/pufereq/simulat/commit/20ec781934984385f38cf29ab608549bf064f5ed) **menu_widget.py**: prepend `locked:` to info of locked entry

### Styling

- [`7ba5ff9`](https://github.com/pufereq/simulat/commit/7ba5ff97714e233b325f4f6a4db9cb9616e4a4b2) **menu_widget.py**: improve code formatting in MenuEntry constructor

## [0.5.0-alpha.2] - 2023-10-26

### Bug Fixes

- [`76b4628`](https://github.com/pufereq/simulat/commit/76b462843ab2d440212172d6258a8b32c609ef53) **container.py**: fix `loop()` not using result included in `WidgetEndLoop` exception

### Features

- [`4cea9b5`](https://github.com/pufereq/simulat/commit/4cea9b5882d37275c0373646b68d1cd5617844f5) **text_input_widget.py**: add `TextInputWidget` class

### Miscellaneous Tasks

- [`389abb3`](https://github.com/pufereq/simulat/commit/389abb3afd1d8a661baf93437740595999730285) **release**: 0.5.0-alpha.2
- [`30a8c66`](https://github.com/pufereq/simulat/commit/30a8c661860b047d1b463603e1cd599618ecb1db) **release-it.toml**: fix error when generating changelog
- [`067a20d`](https://github.com/pufereq/simulat/commit/067a20d2822b61c56894f9ac6781ec120b0d3212) **release_it.yml**: fix error when generating changelog
- [`af27c09`](https://github.com/pufereq/simulat/commit/af27c09c58c368d25ea180454f61d33f59c9989b) **container.py**: remove debug call to `move_relative` with `d` key
- [`0c8d9a2`](https://github.com/pufereq/simulat/commit/0c8d9a262217fde468c729a934abd5331da6ada0) **main.py**: add menu entry for debugging text input widget

## [0.5.0-alpha.1] - 2023-10-22

### Bug Fixes

- [`8e36742`](https://github.com/pufereq/simulat/commit/8e36742a86194cb6be5ea2f2593f5acb46928ba1) **container.py**: fix error when calling `move` method of `Container` class
- [`f990188`](https://github.com/pufereq/simulat/commit/f99018897f7173da5294c4452d4025c762c41077) **menu_widget.py**: fix TypeError when `None` provided as `info` argument in `MenuEntry`
- [`71b6037`](https://github.com/pufereq/simulat/commit/71b6037ab1257ca4b80d054dfb0017cf42fa55ff) **menu_widget.py**: fix TypeError when `None` provided as `description`
- [`13b1939`](https://github.com/pufereq/simulat/commit/13b19392067cbbf6f35e751e1506290c826262fa) **container.py**: fix visual glitch when moving the container
- [`b011ac8`](https://github.com/pufereq/simulat/commit/b011ac803ab29ff25aa191d135357cc7ff9c6dbc) **menu_widget.py**: fix selection bugging out when `self.items` is smaller than `self.MENU_SIZE`
- [`af1b4df`](https://github.com/pufereq/simulat/commit/af1b4df53215fb86de066317a3a9d281eea8234f) **window.py**: fix wrong `beg_y` and `beg_x` being set when `update_size()` called
- [`4b5c67e`](https://github.com/pufereq/simulat/commit/4b5c67e00cabb1da4bce00af325bea1f34380ba1) **container.py**: fix info details appearing only for 0.1 seconds while `GameMap` loaded
- [`a2597bb`](https://github.com/pufereq/simulat/commit/a2597bbdadc9f23a62547e5bb0e0746a174decd3) **main.py**: fix typo in import in `test()`
- [`1a69b6b`](https://github.com/pufereq/simulat/commit/1a69b6b6da6f76d7d3ae803eb4dcd3e93944033d) fix double init of curses
- [`b27ffcc`](https://github.com/pufereq/simulat/commit/b27ffcc6415d1c3e3853c023a12809b892a0ed4b) **window.py**: fix error when `set_title()` calls `window.refresh()` if it's a pad
- [`fa620f8`](https://github.com/pufereq/simulat/commit/fa620f8c4e2b52117bbcfd0cd86f61a4e1743417) **window.py**: fix error when using `addstr()` with `-1` as `y` or `x`

### Documentation

- [`f98a9b4`](https://github.com/pufereq/simulat/commit/f98a9b40daaadcdd7436bd46c82b737072db8bfa) **loop.py**: add docstrings to `game_loop()` and `_loop()`
- [`5eeae4d`](https://github.com/pufereq/simulat/commit/5eeae4d54dc372d7d498eac2fe86f1487e1316fb) **container.py**: add docstrings to `Container` class
- [`31e5f57`](https://github.com/pufereq/simulat/commit/31e5f57ead3bbd5ca00d2a4bab323a123fb07449) **widget.py**: add docstrings to `Widget` class
- [`00ddbca`](https://github.com/pufereq/simulat/commit/00ddbca79d09d15a113f3e0a24bb6c9cd75d5022) **menu_widget.py**: add docstrings to `MenuWidget` class
- [`cdb4b43`](https://github.com/pufereq/simulat/commit/cdb4b4320b0bac26e583d12a8ba94d50a7e55bec) **menu_widget.py**: add docstrings to `MenuEntry` class
- [`69fe85c`](https://github.com/pufereq/simulat/commit/69fe85cc5758c765ba1add0147edc22f7054765f) **game_map.py**: remove incorrect comment
- [`188a61b`](https://github.com/pufereq/simulat/commit/188a61b4a9eecf311ba4db2f40678f1422381528) **game_map.py**: modify comments in `_move_player` method to improve readability
- [`a590dc6`](https://github.com/pufereq/simulat/commit/a590dc66375d22fa4c3a5683235b92ba562e1983) **game_map.py**: add docstrings

### Features

- [`9ef9f0a`](https://github.com/pufereq/simulat/commit/9ef9f0afa8a0b75c5222db7a6afb7e352cea40d9) **menu_widget.py**: make `self.MENU_SIZE` dependent on widget's size
- [`5578607`](https://github.com/pufereq/simulat/commit/5578607f3b87020089d9486aca38974e07812ea6) **container.py**: add `description` field to `Container` class constructor
- [`dd661bf`](https://github.com/pufereq/simulat/commit/dd661bf975b9f205c1b96b007e755a6a74c04e0f) **menu_widget.py**: add `_display_info` method
- [`4c332e3`](https://github.com/pufereq/simulat/commit/4c332e3bb7f99af206be198a72e37527c1f081b4) **menu_widget.py**: add vim keybindings (`j` (down) & `k` (up)) to `_input`
- [`1414dcb`](https://github.com/pufereq/simulat/commit/1414dcb351643eeff416e3035f7a13a86d37aa50) **menu_widget.py**: add ability to change selection using `PageUp` and `PageDown`
- [`20885e3`](https://github.com/pufereq/simulat/commit/20885e352a4ef2349dba2337f1f0fbb1b685dcb6) **main.py**: modify `test()` to now use `MenuWidget` instead of `DebugWidget`
- [`7347bdd`](https://github.com/pufereq/simulat/commit/7347bddb0aae639c78da2d3df98f23056ab1554f) **menu_widget.py**: add a `MenuWidget` class.
- [`e831f05`](https://github.com/pufereq/simulat/commit/e831f05121597ca7dc1d67550e263be4a932541c) **container.py**: add a `loop` method
- [`45a0276`](https://github.com/pufereq/simulat/commit/45a0276833085e512d3367f7969fab9ee1be4558) **container.py**: add `move_relative` method
- [`269e85d`](https://github.com/pufereq/simulat/commit/269e85df76d6ed54ad2937f7da8034bf91a5a002) **container.py**: add `move` method with centering functionality
- [`64824f7`](https://github.com/pufereq/simulat/commit/64824f71d065b19d37ee9a3b5455ab6381b1d5ec) **container.py**: modify name of `draw_widget` to `refresh_all`
- [`dc04e3c`](https://github.com/pufereq/simulat/commit/dc04e3c77fffff80b8921e00e7b48c3adb28cd31) **widget.py**: add `WidgetLoopEnd` Exception class
- [`4bc1d70`](https://github.com/pufereq/simulat/commit/4bc1d70b31b39dd6fb7d1e8bc14593418923e9d9) **widget.py**: add `_wrap_str_to_width` method
- [`b8a4557`](https://github.com/pufereq/simulat/commit/b8a4557e93b447022ba2aa358809d46aece21da4) **window.py**: add `mvwin` method
- [`4e8f810`](https://github.com/pufereq/simulat/commit/4e8f81099fbd42d7cb5417584eb61ea0b96a3c1a) **window.py**: add `erase` method
- [`91adde7`](https://github.com/pufereq/simulat/commit/91adde7850abf25565371c6b724d74708bdaf294) **window.py**: add call to `update_size` in `refresh`
- [`7c4c5d0`](https://github.com/pufereq/simulat/commit/7c4c5d064a73979d83744abcff38ebaa3cd27c94) **window.py**: add `update_size` method
- [`f8aea86`](https://github.com/pufereq/simulat/commit/f8aea867c31bd937460e04a8a5089d941a397364) **window.py**: add `self.beg_y` and `self.beg_x` variables
- [`662f957`](https://github.com/pufereq/simulat/commit/662f95785bd076c7cb7daf8262e4780224a79397) **window.py**: add call to `self.keypad(True)` in `_common_init()`
- [`9f2097f`](https://github.com/pufereq/simulat/commit/9f2097fa864be28f6ec6989220fc8bc16ae63f5b) **map_layout.py**: add call to `main.test()`(the example container) from the `GameMap`
- [`c7bd0a4`](https://github.com/pufereq/simulat/commit/c7bd0a40249b2cdef4a65dbddce5a987f00c2acb) **container.py**: add centering of the container relative to `content_win`
- [`2a2a58f`](https://github.com/pufereq/simulat/commit/2a2a58f18c722a223dfac4583719b954aae2fe4c) **main.py**: move example container to its own function
- [`bb1928d`](https://github.com/pufereq/simulat/commit/bb1928dbfe98c03a58cbefdb0ce7e49f33e19928) **main.py**: add a 'container' button for debugging purposes
- [`d95d230`](https://github.com/pufereq/simulat/commit/d95d230b83d442c0bdb93d9ec621ab74bb2a3723) **debug_widget.py**: add a `DebugWidget` for debugging of `Container` and `Widget` classes
- [`ee340cc`](https://github.com/pufereq/simulat/commit/ee340cc33442c7c994c8f4bc30e493e284443b47) **widget.py**: add `Widget` class
- [`0ae0437`](https://github.com/pufereq/simulat/commit/0ae0437cea680fbb75c73b354881a9b5c85c3b16) **container.py**: add `Container` class
- [`b58f6c8`](https://github.com/pufereq/simulat/commit/b58f6c80f83cb526cde608c4ce97bffe32652180) **window.py**: modify title alignment (center > left)
- [`f1595a9`](https://github.com/pufereq/simulat/commit/f1595a916dd87e18ab9e7a72ec1f1d920b7610d9) **window.py**: add `set_title()` method

### Miscellaneous Tasks

- [`4a707bf`](https://github.com/pufereq/simulat/commit/4a707bfa3369139af09d7dd30d58e77bd89f6b05) **release**: 0.5.0-alpha.1
- [`9b395d4`](https://github.com/pufereq/simulat/commit/9b395d42bc1f9f2d29e1c2f20345266497d39777) **release_it.yml**: add release_it workflow
- [`429542d`](https://github.com/pufereq/simulat/commit/429542d4307eaf17f7a95cb26bef42a4188730da) **release_from_tag.yml**: delete `release_from_tag.yml`
- [`d90e4dc`](https://github.com/pufereq/simulat/commit/d90e4dc227c01d93eb9bdb8c0904a3693ca5a9fa) **bump_version.yml**: remove `bump_version.yml`
- [`16d6e31`](https://github.com/pufereq/simulat/commit/16d6e31aaf4ac5e6c8e7e1d6a6f387b4b985baf1) **.cz.toml**: modify commitizen config to allow for pre-releases
- [`c166a6c`](https://github.com/pufereq/simulat/commit/c166a6c7e5bf6e10b5b5340f9e71321bb3e1a85a) **release_from_tag.yml**: add release from tag workflow
- [`e2eb19c`](https://github.com/pufereq/simulat/commit/e2eb19c8384838deb0ee9821945dc49c9ac77458) **main.py**: modify imports and calls from `test()` to `container_test()`
- [`f99a14e`](https://github.com/pufereq/simulat/commit/f99a14e0113ca304621740ff0dd818f04f8480e7) **container.py**: modify `Container.loop()` to respect new timeout set in loop.py
- [`ec8473b`](https://github.com/pufereq/simulat/commit/ec8473bc74026fb0e9222c9ecf978cb005d1f418) **loop.py**: split main loop from handler
- [`b11ec6c`](https://github.com/pufereq/simulat/commit/b11ec6cfe806a830b5921cfab9db7682c9810713) **game_loop**: improve frame timing
- [`bbb3a71`](https://github.com/pufereq/simulat/commit/bbb3a7157c49c3ed1e0c39ede85762477b86023f) **map_layout.py**: modify import and reference to point to `container_test()` function in container.py
- [`0d11156`](https://github.com/pufereq/simulat/commit/0d111564d65525a057d8590f9ad5d9a4506f4fd9) move `test()` from main.py to `container_test()` in container.py
- [`d3428ea`](https://github.com/pufereq/simulat/commit/d3428eaeeb19d46a61cc074a64cfdd126fc103c5) **main.py**: make main menu smaller
- [`a41e7a0`](https://github.com/pufereq/simulat/commit/a41e7a04d43f7d6f12f3609863fffd7379f0c3ea) **menu_widget.py**: add return prompt to info display
- [`3a246c5`](https://github.com/pufereq/simulat/commit/3a246c5e5b840b95946d922e8ac36454beec4082) **menu_widget.py**: modify entry label display in info view to increase UI readability
- [`1bbacb1`](https://github.com/pufereq/simulat/commit/1bbacb1a7d5f9307990160ca62c116a47a0f951f) **menu_widget.py**: modify `display` method to center menu entries in container
- [`5110ab7`](https://github.com/pufereq/simulat/commit/5110ab7cb93b50c2a13e27511a39d28372999017) **container.py**: move `content_win` import into `Container` class constuctor
- [`514e951`](https://github.com/pufereq/simulat/commit/514e9518bb95559a4e8cbc05908b5bef15566ee2) **menu_widget.py**: reduce spacing between info title and info text
- [`92f48dc`](https://github.com/pufereq/simulat/commit/92f48dc98630966ea28d53c98086c8a186a98b8e) **main.py**: modify `Container`'s `nlines` argument to make it bigger
- [`6680fb7`](https://github.com/pufereq/simulat/commit/6680fb7c46b376975d9b1b86f2667e5ccfdd4cdf) **main.py**: add `description` argument in call to `Container`
- [`4221466`](https://github.com/pufereq/simulat/commit/422146665428895d84d2e90d8e45a709e0fc4cab) **widget.py**: modify size and position of widget to make space for `Container`'s description
- [`4182086`](https://github.com/pufereq/simulat/commit/4182086328b744c1b4ed19cde061db1b39324a49) add `.mailmap`
- [`54cf308`](https://github.com/pufereq/simulat/commit/54cf308ab13132d65cc448b349156969cf4ed2b2) **requirements.txt**: remove unused dependecies
- [`9c01a40`](https://github.com/pufereq/simulat/commit/9c01a4082a461d2fadefb68f433a2355a4445b08) **.gitignore**: add `env` folder to gitignore
- [`5cabae2`](https://github.com/pufereq/simulat/commit/5cabae29c1c018418f6888a806791feb3c8f4cf4) **bump_version.yml**: auto releases are drafts for modifications to body

### Refactor

- [`7c56573`](https://github.com/pufereq/simulat/commit/7c56573532ffb3d78060d18b664859eb4b32a9ef) **main.py**: modify `main_menu` to use `Container` and `MenuWidget` instead of old `Menu` class

### Styling

- [`941770d`](https://github.com/pufereq/simulat/commit/941770d024bef9c19c580849639188a8670d16d8) **container.py**: move list comprehensions below for better readability
- [`cbd0283`](https://github.com/pufereq/simulat/commit/cbd02838ab9dee2997e07e4744723e49f307898f) **game_map.py**: remove commented-out code

### Build

- [`bbdb04c`](https://github.com/pufereq/simulat/commit/bbdb04c930d224c9835c43a1ff98e540480260e4) **.release-it.toml**: add `.release-it.toml`
- [`32c0c0b`](https://github.com/pufereq/simulat/commit/32c0c0b45280ca16d137462197ec33828f6c505c) **requirements.txt**: add `requirements.txt`

## [0.4.0] - 2023-09-06

### Bug Fixes

- [`17c8c79`](https://github.com/pufereq/simulat/commit/17c8c7937e28f8fed98e5141ea1253fe86f423bc) **game_map.py**: fix player moving when camera move called
- [`f94cfc1`](https://github.com/pufereq/simulat/commit/f94cfc1f64bb4e9734030a176722d291068e59a8) **game_map.py**: fix door glitching when interacted while door's position = player's position
- [`fe32fc5`](https://github.com/pufereq/simulat/commit/fe32fc514c6a3624216ac457a867bd7308686cfd) **door.py**: fix `__repr__()` not returning a string
- [`57f37ed`](https://github.com/pufereq/simulat/commit/57f37ed1d5560925aa04cd1728e41174ada0b9ba) **game_map.py**: fix pad restricting map by being too small
- [`6d2338f`](https://github.com/pufereq/simulat/commit/6d2338ff64cb19c533ecc2ec1807da901c86effd) **game_map.py**: fix typo in calculation of `self.max_displayed_pad_size` in `_resize()` method
- [`68d9980`](https://github.com/pufereq/simulat/commit/68d9980efd840c01bce5097e816857fe2c749134) **game_map.py**: adjust `pad_view_left` and `pad_view_top` calculations
- [`6c92c30`](https://github.com/pufereq/simulat/commit/6c92c30cd3e03e5fb6a8a8e40667a7931e21ef59) **game_map.py**: fix title not being displayed properly on topbar
- [`9faeef4`](https://github.com/pufereq/simulat/commit/9faeef4835f63778e9387ecfe699793291478dc1) **game_map.py**: fix pad not spanning whole terminal
- [`57f3ac1`](https://github.com/pufereq/simulat/commit/57f3ac1b8d14efea1660ddb5c6d00878550bfab3) **game_map.py**: fix player leaving behind a black box when moving first time
- [`51ea090`](https://github.com/pufereq/simulat/commit/51ea0904441ca0c3e321fcb4396a9a57e5a79627) **game_map.py**: fix player not appearing when map loaded
- [`8370b48`](https://github.com/pufereq/simulat/commit/8370b4896b6e426fbaf297ef65d442cd810fc2ab) **init.py**: fix AttributeError when calling content_win.panel
- [`a8994e3`](https://github.com/pufereq/simulat/commit/a8994e3552c4700bbaf23221d115caf775c87c60) **game_map.py**: fix error when going out of negative bounds
- [`027bc3e`](https://github.com/pufereq/simulat/commit/027bc3e493bc8a53bc9c9efd0916e90467ea122b) **game_map.py**: fix screen flicker when moving
- [`fd8defe`](https://github.com/pufereq/simulat/commit/fd8defec85db7a5bb968f7af16983e2b22422afb) **menu.py**: fix menu disappearing when content_win.panel's window replaced

### Documentation

- [`6efb018`](https://github.com/pufereq/simulat/commit/6efb018d0126ba464f8368f8b3cf96a3f2329b62) **game_map.py**: add missing comment

### Features

- [`83e5ab7`](https://github.com/pufereq/simulat/commit/83e5ab7e580a5416895c1cfdc2462a504dd7bc8b) **game_map.py**: add camera controls
- [`cda006f`](https://github.com/pufereq/simulat/commit/cda006f9dd5d0f6624c03cfa4ac277484123d4e2) **game_map.py**: modify `GameMap()` class to use cell classes
- [`0e6f26b`](https://github.com/pufereq/simulat/commit/0e6f26b1562770e5fdc65502c4c008d04a82a320) add cell classes
- [`e054edb`](https://github.com/pufereq/simulat/commit/e054edbbc570f9af9d9106f6490d51847d17c4a7) **game_map.py**: replace `INTERACTIONS` with `self.interactions` in `_interact()` to avoid possible conflict
- [`8f5a9e9`](https://github.com/pufereq/simulat/commit/8f5a9e9237daa14d9cc41311494d85a47994be13) **map_layout.py**: add some doors to the map for showcase
- [`d4020be`](https://github.com/pufereq/simulat/commit/d4020be620908a5f6a63819e4946a6795b68be52) **map_layout.py**: add functionality to `example_action()`
- [`5555d4d`](https://github.com/pufereq/simulat/commit/5555d4d5d1e3b1387ed5055d62416c8de472b68a) **game_map.py**: modify behavior of interacting with interactions to be more intuitive
- [`0a76854`](https://github.com/pufereq/simulat/commit/0a76854d871f76c2761ddda5c143db9ab43e9a06) **init.py**: change floor color to be more realistic
- [`ffb26fd`](https://github.com/pufereq/simulat/commit/ffb26fd43674c2b38d564cc0b175ee17827fe138) **init.py**: add colors for door characters
- [`affd599`](https://github.com/pufereq/simulat/commit/affd5990e80245001d943382ce33722ea17f8f0d) **game_map.py**: add door character `"d"` and `"D"` which use `Door()` class
- [`9e7d059`](https://github.com/pufereq/simulat/commit/9e7d059e60d1f8b7ad567e074f58eaf7911a41da) **door.py**: add `Door()` class
- [`6a6f879`](https://github.com/pufereq/simulat/commit/6a6f8791882ba8d663f0434f5bc44861b845c0e0) **map_layout.py**: add floor to building
- [`f6de40a`](https://github.com/pufereq/simulat/commit/f6de40afc3418d83d4b2d058e6b5df56b82b351d) **game_map.py**: modify texture of floor to add knots and cracks
- [`baa344f`](https://github.com/pufereq/simulat/commit/baa344fd5eff9094b0cbdd28725c524d81bc4bdb) **game_map.py**: modify `self.grass_chars` for more realism
- [`650b050`](https://github.com/pufereq/simulat/commit/650b050043d9d976048cfa1eaa043b4cc5e73dd6) **game_map.py**: add coordinates to `topbar.details_win`
- [`9582b5a`](https://github.com/pufereq/simulat/commit/9582b5af90291da1674f3cf06d4d51c16c68d24d) **init.py**: modify color of `GRASS_PAIR`
- [`33abc04`](https://github.com/pufereq/simulat/commit/33abc04a86fcc45fd9e9d06c3296149a33b7ea4f) **game_map.py**: modify not specified cells to be grass in _map_init()
- [`24824cc`](https://github.com/pufereq/simulat/commit/24824cc93c715783ee1e483a0ef1dfc6625f5e8a) **game_map.py**: improve grass rendering
- [`cec44b7`](https://github.com/pufereq/simulat/commit/cec44b7e68c34bbb3206fc1c35d4dacb2ff32050) **game_map.py**: utilize color; add floor, grass char
- [`6c72948`](https://github.com/pufereq/simulat/commit/6c729486334ba859f9192dcf5300e433a7354682) **init.py**: add color support
- [`9fb1a79`](https://github.com/pufereq/simulat/commit/9fb1a795b6e974288e2f0a4e0d64b3321e2d8e06) **game_map.py**: modify _move_player() to restore the original character before moving the player
- [`9a7f5b0`](https://github.com/pufereq/simulat/commit/9a7f5b067c9110c865f6bb7c94227f785904a793) **game_map.py**: change _draw_map() to set attribute of interactive chars to cs.A_REVERSE
- [`1ec687e`](https://github.com/pufereq/simulat/commit/1ec687e69136c1143c83fdf377303b91c2e40b28) **game_map.py**: change interaction behavior
- [`5bec804`](https://github.com/pufereq/simulat/commit/5bec8044ebddbf587dcea3ea46a818da445104af) **loop.py**: add game_map._refresh_map() call
- [`508e82d`](https://github.com/pufereq/simulat/commit/508e82d1f992c79c43a4433efa6c6d56068ecd3b) **loop.py**: add terminal resize handling
- [`6cf55e3`](https://github.com/pufereq/simulat/commit/6cf55e3c544962dec89802247f201f0ebe65a05a) **game_map.py**: add _resize method
- [`5397dae`](https://github.com/pufereq/simulat/commit/5397dae778c0d3ff396d9be95f6fe6cbb876fcf0) **loop.py**: handle keypresses directly from loop and use new arguments in call to game_map._input()
- [`4aa48bf`](https://github.com/pufereq/simulat/commit/4aa48bf6ce0857c7aecec208b2ea2081221210f8) **game_map.py**: add _refresh_map() method for future use
- [`8e2f084`](https://github.com/pufereq/simulat/commit/8e2f084f48b13a1ca59c58a5c1ff81db57559d29) **game_map.py**: make _input() accept key presses as argument to work with game_loop()
- [`16d9786`](https://github.com/pufereq/simulat/commit/16d9786c0c8da4a2283a5c832db850e82780ddf0) **game_map.py**: limit camera to not exceed positive map limit
- [`064499f`](https://github.com/pufereq/simulat/commit/064499fe73d634831aac69dbe0940a423f9f5db1) **main.py**: modify main_menu() to call game map
- [`282c831`](https://github.com/pufereq/simulat/commit/282c8313c73d184a5e16b931885004458b06ed54) **init.py**: add init_game_map()
- [`474cfd8`](https://github.com/pufereq/simulat/commit/474cfd8f82d6e4b3f9049ead1db53e3e91a1b73d) **loop.py**: add game loop
- [`22b9139`](https://github.com/pufereq/simulat/commit/22b9139447e63119d8847f5c8aae505b4b1452bf) **map_layout.py**: add map layout
- [`eaf95b4`](https://github.com/pufereq/simulat/commit/eaf95b4381643c467d58af845ed49e88245fac93) **game_map.py**: add open world
- [`f01ea15`](https://github.com/pufereq/simulat/commit/f01ea154629f557a4288d15da4c7f060fc8dea64) **pad.py**: add curses pad support
- [`a483978`](https://github.com/pufereq/simulat/commit/a483978a59044ef82487f5fe99a5db25c5c946db) **window.py**: add *args and **kwargs for future pad management
- [`6039d19`](https://github.com/pufereq/simulat/commit/6039d19305ec4bb737dd550b15548a64dc9fb9cb) **window.py**: remove refresh() calls from border() and addstr() for more classic behavior

### Miscellaneous Tasks

- [`7e155d4`](https://github.com/pufereq/simulat/commit/7e155d47ecea9a2266d8926ddd1038aa9953de6e) **game_map.py**: remove unnecesarry imports
- [`578071a`](https://github.com/pufereq/simulat/commit/578071a35f0f26159781bebdc1c329174fc7ca61) **cell.py**: remove unnecessary imports
- [`b630e60`](https://github.com/pufereq/simulat/commit/b630e604819c3ef444284f9846e33d7087f1e273) **door.py**: remove obsolete door.py
- [`6997777`](https://github.com/pufereq/simulat/commit/69977777285d7b6cd10730924f0f7209c64715b5) **.cz.toml**: add missing space

### Refactor

- [`f7b150e`](https://github.com/pufereq/simulat/commit/f7b150e5ca2784625c0d6d6026e1f720ce4ae0f4) refactor curses initialization
- [`255bcc0`](https://github.com/pufereq/simulat/commit/255bcc02d1b8461b2419ef9380cdd2d4a689dd90) **game_map.py**: change variable name
- [`d6db94e`](https://github.com/pufereq/simulat/commit/d6db94eab0866e81b29a3f5829667ecdec8927c8) **game_map.py**: remove unnecessary additions in self.pad_size

### Styling

- [`fec5543`](https://github.com/pufereq/simulat/commit/fec55432580ed0d0ee5552ea5a82f086b3d1f40c) **game_map.py**: split import of `*COLOR` from `simulat.core.init` for better readability
- [`59c64f5`](https://github.com/pufereq/simulat/commit/59c64f5a57c234062b200b9f6a5bfefbf41ebd21) **game_map.py**: add inline comment at `self.MAP_SIZE` definition
- [`7d2cb14`](https://github.com/pufereq/simulat/commit/7d2cb14cefa98e85d6158cb6de0ef76f3a5cf5f4) **game_map.py**: add comments
- [`826828c`](https://github.com/pufereq/simulat/commit/826828c9e5063f2ab0b595404391a5c41a25a530) **loop.py**: add spacing before function definition
- [`cb5c956`](https://github.com/pufereq/simulat/commit/cb5c9562520c9536809020fb60aa9fc922174585) **game_map.py**: remove commented code

## [0.3.0] - 2023-07-31

### Bug Fixes

- [`e018f85`](https://github.com/pufereq/simulat/commit/e018f851cf7e9fc7ee534b3035d8a511ee0d15d7) **menu.py**: fix borders not appearing
- [`5ebe110`](https://github.com/pufereq/simulat/commit/5ebe110ff2a3fec7eabb2f1c05e7c305ceba675a) **error_handler.py**: fix retrying not working correctly

### Features

- [`d896b04`](https://github.com/pufereq/simulat/commit/d896b0443d755bc01f528727046639640cbad609) **board.py**: limit max movement speed
- [`fad8c00`](https://github.com/pufereq/simulat/commit/fad8c001cca42858e411c89eff36dda4854d630a) **init.py**: make content_win not a panel
- [`757df41`](https://github.com/pufereq/simulat/commit/757df413aa41d2ef78aa8b49753e3510b9520c0c) **window.py**: update calls to SubWindow and DerWindow to include named args
- [`1b15cf2`](https://github.com/pufereq/simulat/commit/1b15cf2d8f1b864593f59d436f9a689e58df433b) **window.py**: make make_panel and reverse named arguments
- [`7a009d1`](https://github.com/pufereq/simulat/commit/7a009d17e3e826f46dd42553be04ff8e3f6cb0f2) **derwindow.py**: make make_panel and reverse named arguments
- [`06bdd65`](https://github.com/pufereq/simulat/commit/06bdd6513895f2bc481e658dec8adc0a81e7b688) **subwindow.py**: make make_panel and reverse named arguments
- [`ce6b8bd`](https://github.com/pufereq/simulat/commit/ce6b8bd6a55657b823776319a6d67b5c91d132a8) **subwindow.py**: move addstr() and cs_addstr() to window.py
- [`2da110b`](https://github.com/pufereq/simulat/commit/2da110be70760fc76b9ae35943ded50cfd98bde9) **error_handler.py**: make full_path cleaner
- [`6390750`](https://github.com/pufereq/simulat/commit/6390750584804710ede6bfb12897fa68cf2fbe1f) **main.py**: use error_handler on main_menu()
- [`42e9379`](https://github.com/pufereq/simulat/commit/42e93798e0f7b083848149096c5b6a4443359f2f) **error_handler.py**: make exception menu description more concise
- [`ccb9113`](https://github.com/pufereq/simulat/commit/ccb9113dd04ac5ab23f645ff92e10cadfbeae6b7) **error_handler.py**: add retry option for caught exceptions
- [`3f3a9d8`](https://github.com/pufereq/simulat/commit/3f3a9d8ba424636890820caa737d04b618ca283f) **derwindow.py**: add DerWindow class
- [`01e0d15`](https://github.com/pufereq/simulat/commit/01e0d15861ab660e16092fa3ca29b331107342ba) **subwindow.py**: use _common_init() inherited from Window()
- [`b9a2c16`](https://github.com/pufereq/simulat/commit/b9a2c1666083b06c5e10145c602288d5cd0b863d) **window.py**: add _common_init() to remove duplicate code

### Miscellaneous Tasks

- [`f37004b`](https://github.com/pufereq/simulat/commit/f37004bfb83bd6cdb600b1d760f82dbb85110061) **topbar.py**: include named args in call to Window()'s init
- [`797dee5`](https://github.com/pufereq/simulat/commit/797dee59ac268f33ab7af814fc4d3b8b7b36ff75) **menu.py**: include make_panel argument in player_window and board_window
- [`e95b3a4`](https://github.com/pufereq/simulat/commit/e95b3a47e886823bdfe9e06e4bb22677197a0a9d) **menu.py**: change parent of description_window
- [`d581521`](https://github.com/pufereq/simulat/commit/d58152154fc7dcdee9882d164255580675560759) **menu.py**: include make_panel argument in description_window and info_window
- [`378bc10`](https://github.com/pufereq/simulat/commit/378bc101aeced4ac9b5c5901eb25b84fb5ed4ce6) **.cz.toml**: add bump_message config

### Refactor

- [`80844e3`](https://github.com/pufereq/simulat/commit/80844e3699576d6496c824258ee96d18efcbc178) **menu.py**: implement window management on info_window and info_window_border
- [`9630814`](https://github.com/pufereq/simulat/commit/9630814d18284375e9d5c6dd207fdc475795c062) **menu.py**: make description_window_border and description_window DerWindows
- [`8f515f5`](https://github.com/pufereq/simulat/commit/8f515f55ac1e31a1cd98967bcf79d58ae34bae8d) **menu.py**: make root_window and root_window_border Windows instead of SubWindows
- [`00d7f01`](https://github.com/pufereq/simulat/commit/00d7f01b028f94c45d980ca1e56bf1f3bdbe3bcf) **menu.py**: remove unused code
- [`89441af`](https://github.com/pufereq/simulat/commit/89441afb134213967c36632c1f0b83d1853a697e) **menu.py**: use f-string padding for label formatting

### Styling

- [`2897355`](https://github.com/pufereq/simulat/commit/28973554b37d71bf1a16ca62325e5f547ebf59ad) **bump_version.yml**: remove trailing whitespace

## [0.2.0] - 2023-06-22

### Bug Fixes

- [`0444637`](https://github.com/pufereq/simulat/commit/04446374bc386f8d62cd8d84bfe91c2c029b166e) **bump_version.yml**: use new token
- [`6e48aaa`](https://github.com/pufereq/simulat/commit/6e48aaa93f1a1f1ee9268e8bfde38cb20fc09f3f) **bump_version.yml**: add permission bypass to omit branch protection
- [`90c6508`](https://github.com/pufereq/simulat/commit/90c650807b8b805a3a0473c89104bd973397fe4d) **bump_version.yml**: change token back to default
- [`7ded37b`](https://github.com/pufereq/simulat/commit/7ded37b22611d4308040a71cf654e52cedc56bc7) **bump_version.yml**: fix permission denied when creating tag
- [`c1ea05d`](https://github.com/pufereq/simulat/commit/c1ea05dda44a7f308bc8b6083ff4d40ccc051fca) **bump_version.yml**: omit error when signing tag
- [`5800675`](https://github.com/pufereq/simulat/commit/5800675099f78f62e42a4004ec18d8ff9272dc1b) **subwindow.py**: fix error when using addstr() in a nested subwindow
- [`fec6a6a`](https://github.com/pufereq/simulat/commit/fec6a6a0a22548169b12693c7dbd2cdb403ae327) **subwindow.py**: fix error when nesting subwindows
- [`c770c2c`](https://github.com/pufereq/simulat/commit/c770c2c6a5ddb8370b3f15a82034e8fe85233ff7) **window.py**: variable name typo

### Documentation

- [`f9abb3c`](https://github.com/pufereq/simulat/commit/f9abb3c8c712f9bdf652db1c421fe398c24ee229) **PULL_REQUEST_TEMPLATE.md**: add PR template
- [`7e2d41c`](https://github.com/pufereq/simulat/commit/7e2d41c66c6c65eed1cdc96e41f968a6f4e72967) **CHANGELOG.md**: rewrite changelog
- [`37822cf`](https://github.com/pufereq/simulat/commit/37822cfd1bf650e230edbf29d666948ddfdc70b5) **board.py**: remove typo in docstring
- [`ecfa564`](https://github.com/pufereq/simulat/commit/ecfa56498f9d32a618b7981ab540cd420652b4a4) **README.md**: correct wakatime link
- [`bd6d8b9`](https://github.com/pufereq/simulat/commit/bd6d8b9204956b09546c0b32ae9c7738a871474a) **README.md**: add wakatime stats

### Features

- [`367c10d`](https://github.com/pufereq/simulat/commit/367c10dd32ff531efcea96b2205055bdb508c4cd) **board.py**: add error_handler decorators
- [`304708c`](https://github.com/pufereq/simulat/commit/304708c2ef46f36e380ad7dcf111436ce8defb59) **main.py**: add error_handler decorator back
- [`14a316a`](https://github.com/pufereq/simulat/commit/14a316ac6254347951d4fd8668b882598f1be658) **.cz.toml**: remove gpg_sign
- [`9b2dc18`](https://github.com/pufereq/simulat/commit/9b2dc180449bf36ddcb76425635ae9d6f20ad043) **bump_version.yml**: comment out gpg key import
- [`0e1fa17`](https://github.com/pufereq/simulat/commit/0e1fa17d6baf441a46209c1a7699ea934646083a) **board.py**: implement window management
- [`723fc19`](https://github.com/pufereq/simulat/commit/723fc195e4f4d06cd53b1b08530764b8b7117f00) **window.py**: add insch() method
- [`c636ec6`](https://github.com/pufereq/simulat/commit/c636ec69b8a8249e3e69cbe9af4e5c271bc1d6e5) **menu.py**: implement window management
- [`a34fd87`](https://github.com/pufereq/simulat/commit/a34fd87970640e0d8e4a10cfe24a7c947e41e9aa) **subwindow.py**: add cs_addstr method
- [`32e8c82`](https://github.com/pufereq/simulat/commit/32e8c8252cc22d4640ea1e5e10cc4931146452be) **init.py**: implement window management
- [`1c6eb78`](https://github.com/pufereq/simulat/commit/1c6eb78fbdfaa21be182f2f1c603159f84fbb3de) **window.py**: add curses methods to Window via encapsulation
- [`71d0ec8`](https://github.com/pufereq/simulat/commit/71d0ec8ff14cdae93fca7c91e855851110ab6cb1) **window.py**: add curses.panel support
- [`6dc8cf9`](https://github.com/pufereq/simulat/commit/6dc8cf9588d32525840c9cbaf07f57708a5f7436) **subwindow.py**: add curses.panel support
- [`3f77f5e`](https://github.com/pufereq/simulat/commit/3f77f5e73614ce68d68eb9ee73f30dff72c4fcbc) **board.py**: update topbar call to match new implementation
- [`874ba37`](https://github.com/pufereq/simulat/commit/874ba37b5420d1b7e330cf5e0c0673c44b924c14) **main.py**: update topbar call to match new implementation
- [`30588d2`](https://github.com/pufereq/simulat/commit/30588d23bd4054ef3ef3cd07b590be93aba04e29) **window.py**: add support for curses atrributes in whole window
- [`8f20599`](https://github.com/pufereq/simulat/commit/8f205992bcb2c96802e58dc3dc93e458caf731d9) **topbar.py**: implement window management
- [`b2773b8`](https://github.com/pufereq/simulat/commit/b2773b8d0ac5aa8edc0187a8078ad3e76ecdc277) **subwindow.py**: add right alignment of text
- [`df3ce73`](https://github.com/pufereq/simulat/commit/df3ce73353bd2a8c4e4da30eb0eb443d34581b03) add window management
- [`9e16302`](https://github.com/pufereq/simulat/commit/9e163029f6d3693038b95a155fec9f3d0ec03a42) **board.py**: add curses.beep when interacted with a collider
- [`46bb23e`](https://github.com/pufereq/simulat/commit/46bb23e89418d818a414405a2a16316da5ec2624) **board.py**: add support for displaying board title on topbar

### Miscellaneous Tasks

- [`1adc6a0`](https://github.com/pufereq/simulat/commit/1adc6a0c2d7d8bcaa999bd01b0224600a20485c5) **bump_version.yml**: run job if executed manually
- [`4b362f8`](https://github.com/pufereq/simulat/commit/4b362f845241065d39ec76d15c1b3e32b8de68a6) **bump_version.yml**: add manual execution
- [`49226e5`](https://github.com/pufereq/simulat/commit/49226e516d26b2c1e18ecddb847dd79b9949709b) **bump_version.yml**: add push argument to commitizen
- [`3fb1f69`](https://github.com/pufereq/simulat/commit/3fb1f69763dcba0a36b49f4b522f15574de759f5) **.gitignore**: remove .simulat_old
- [`42ff481`](https://github.com/pufereq/simulat/commit/42ff4815695b24464ec280e3ec3de80af0ec5f4e) **bump_version.yml**: change job to run only if 'gh-release' present
- [`f0b564c`](https://github.com/pufereq/simulat/commit/f0b564cc4edc07035b9331e486cccce8fc672c82) **actions/bump_version.yml**: add gpg signing of bump commit
- [`e786785`](https://github.com/pufereq/simulat/commit/e786785e733eb779a887a8af11f23941a4382f4a) **actions/bump_version.yml**: auto release after bump
- [`3ffcf5d`](https://github.com/pufereq/simulat/commit/3ffcf5d965106228117ca00c73dd5bc8efcf0bba) **actions**: add commit_check.yml
- [`c672e28`](https://github.com/pufereq/simulat/commit/c672e2892602c3e4d18d35ac41ca7519c5d33df5) add .github/workflows/bump_version.yml
- [`017ef02`](https://github.com/pufereq/simulat/commit/017ef020624b1f2f13dd2a78fd6f928b0fb56218) **.cz.toml**: add gpg_sign and annotated_tag to commitizen config
- [`8ae0247`](https://github.com/pufereq/simulat/commit/8ae0247804c3bde1cde100573206f6e2271dc980) add commitizen pre-config hook
- [`16678eb`](https://github.com/pufereq/simulat/commit/16678eba8074fd1158c9d061f553eca0fe2064e7) add __init__.py

### Refactor

- [`dc57c9d`](https://github.com/pufereq/simulat/commit/dc57c9da9f4702953b5dd04605863dde04a28934) **.cz.toml**: remove commented code
- [`4b6647c`](https://github.com/pufereq/simulat/commit/4b6647c45886e28d79a294958d489d61a8a05b1d) **window.py**: remove unnecesarry blank lines
- [`a820d55`](https://github.com/pufereq/simulat/commit/a820d55e14369f89cd5ef95a2affd4b1fbac8e56) **window.py**: fix whitespace in function definitions
- [`d3d4473`](https://github.com/pufereq/simulat/commit/d3d447332b73efe346866fe65c08e90f5c0db97a) **topbar.py**: [**breaking**] remove obsolete clear* and update* functions
- [`13ca4c1`](https://github.com/pufereq/simulat/commit/13ca4c133ad18cef7ccbd0e09ad8d3b87b1d91f1) [**breaking**] move simulat/core/windows to simulat/core/ui/windows

### Bump

- [`13f916f`](https://github.com/pufereq/simulat/commit/13f916fd8d6c2c285800827d14a499e79ea541fb) version 0.1.0 → 0.2.0

## [0.1.0] - 2023-04-15

### Bug Fixes

- [`6bef999`](https://github.com/pufereq/simulat/commit/6bef999f9c03c11b20ff343158e15cb710cf6611) **board.py**: fix error when only one of 'args' and 'kwargs' provided
- [`4065498`](https://github.com/pufereq/simulat/commit/40654985f1a25224e2232d192c4abeac9b102245) **menu.py**: fix error when only one of 'args', 'kwargs' provided
- [`1145df9`](https://github.com/pufereq/simulat/commit/1145df9d3da7974e42ac06f690832b9cf9f6cf0f) **menu.py**: fix button padding
- [`a9a6e4e`](https://github.com/pufereq/simulat/commit/a9a6e4e93faef457ac2ad262301d51996c9b194c) **menu.py**: fix error when centered = True
- [`4e211e6`](https://github.com/pufereq/simulat/commit/4e211e6062ab1da6cc28a1aa6bdf2993aa3b4278) **board.py**: fix arrow keys not working
- [`ec85c29`](https://github.com/pufereq/simulat/commit/ec85c29c33c22979f5eb8ac27da9581a48045b78) **board.py**: fix '@' character visible in corner

### Documentation

- [`4fafdbe`](https://github.com/pufereq/simulat/commit/4fafdbe9b850791a2e3d712ebebef047fca81559) **board.py**: update docstrings
- [`be92780`](https://github.com/pufereq/simulat/commit/be92780afeac1425d37b0bc30240b54482c8bf4c) **board.py**: add docstrings

### Features

- [`d555c17`](https://github.com/pufereq/simulat/commit/d555c17a065a95235d8af2f084bbbad956b12cd9) **example.py**: add Board() examples
- [`6a09a5f`](https://github.com/pufereq/simulat/commit/6a09a5fa3439e8d3e0a8990313852cda8f4bd3f8) **main.py**: add label to 'board' item in main menu
- [`3d59ce9`](https://github.com/pufereq/simulat/commit/3d59ce9aa662ada4e1fa86d3313532661793cf65) **main.py**: change 'board' target to display example board
- [`bd13025`](https://github.com/pufereq/simulat/commit/bd13025addcf7186acf94e708bd115ad748852d6) **board.py**: add title rendering
- [`6e657d3`](https://github.com/pufereq/simulat/commit/6e657d3a1130c7b638e92fb775f96d15e121c147) **menu.py**: add support for both args and kwargs in one target
- [`f25823e`](https://github.com/pufereq/simulat/commit/f25823e4c6a712c3fe26180b14986eb0288bcc57) **board.py**: add support for doors
- [`5d280f9`](https://github.com/pufereq/simulat/commit/5d280f9d888ae2b9690b81e45e70708efffec0c0) **board.py**: extend door characters
- [`580ae70`](https://github.com/pufereq/simulat/commit/580ae70ce8ecb5de4ad554f0781dd92ad47566ef) **__init__.py**: add __init__.py
- [`2a1722d`](https://github.com/pufereq/simulat/commit/2a1722d9278a1a0beda1329c7244c13a53a59fe6) **main.py**: add board item to main menu for debigging purposes
- [`e406cfc`](https://github.com/pufereq/simulat/commit/e406cfc5c783eddc21e1b00112c3b8a68f23ee77) **board.py**: add support for custom board actions
- [`856103d`](https://github.com/pufereq/simulat/commit/856103df36f70f40794ba74e4121e8316006d6f2) **board.py**: add board manager

### Miscellaneous Tasks

- [`70622f9`](https://github.com/pufereq/simulat/commit/70622f90c335ca7754469356d020281d0c8bf2b2) version bump

### Refactor

- [`a195fc3`](https://github.com/pufereq/simulat/commit/a195fc387b3527853df883ed66bea4cf57e6e8aa) **board.py**: remove unnecesarry import and unused variable
- [`3e91e27`](https://github.com/pufereq/simulat/commit/3e91e279b3085dde5b8cd986a6d4a33be2a38f75) remove debug function
- [`c15cff1`](https://github.com/pufereq/simulat/commit/c15cff1e392878e33b244bb006d694dcd9d0bbab) **board.py**: change variable name board_str -> board_layout

### Styling

- [`f53a030`](https://github.com/pufereq/simulat/commit/f53a030d6b750b71ed85183074bcb3ab551f36d7) **board.py**: remove commented out code
- [`5bcf12f`](https://github.com/pufereq/simulat/commit/5bcf12f207b1a9690c1d783849e057ea826c9175) **board.py**: change variable names to meet style requirements

## [0.1.0-dev.2] - 2023-03-31

### Documentation

- [`66057b0`](https://github.com/pufereq/simulat/commit/66057b038b0b3d51b8ca5a595c675ddd7be16e9c) **changelog**: add CHANGELOG.md
- [`9c5d902`](https://github.com/pufereq/simulat/commit/9c5d902bc895244ebf35c2f54890bbf1b2aedcf8) **readme**: add CodeFactor badge for develop branch

### Features

- [`2149ca4`](https://github.com/pufereq/simulat/commit/2149ca45ba3c2339506ee3adc1df53541a54fe99) **main.py**: remove debug code
- [`739ca8a`](https://github.com/pufereq/simulat/commit/739ca8a18d07fc594cffaa7eb33ddab76931ab12) **menu.py**: correct info window position
- [`9ea323a`](https://github.com/pufereq/simulat/commit/9ea323a28bb3ac455e619dc498ce0d4a66964b25) **menu.py**: correct button spacing and remove unnecessary code
- [`c0efd81`](https://github.com/pufereq/simulat/commit/c0efd812c48e8ba7818ac4044152a2dc29aab6cf) **menu.py**: update menu layout and info window width calculation to center properly
- [`9fd53e3`](https://github.com/pufereq/simulat/commit/9fd53e3d4d015f80f38f0ee9e399246fbe6b9b9c) add 'raise an  exception' button
- [`2190b61`](https://github.com/pufereq/simulat/commit/2190b6171c8843843d8d88875b84b4b98e4d237a) **core**: add error handler
- [`3aa87a7`](https://github.com/pufereq/simulat/commit/3aa87a7ad13b805c89274f5873d33e3c0a2eac44) **ui**: add support for newlines in menu handler
- [`c2ca936`](https://github.com/pufereq/simulat/commit/c2ca936aa584038f16cab981e027435d3deaaca4) **ui**: clear menu windows upon cleanup
- [`83ff785`](https://github.com/pufereq/simulat/commit/83ff785678e628693bacc35480e77ca8e5f6f7ad) **ui**: widened menu from 40 to 50 characters
- [`62c69be`](https://github.com/pufereq/simulat/commit/62c69be92d912fea0e44dce49410d02d7ee02857) add exit option in main menu
- [`de5c54a`](https://github.com/pufereq/simulat/commit/de5c54ade7dc8f9acab8aec8d752567e56c82b12) **ui**: add ability to describe buttons in menu handler
- [`e34302d`](https://github.com/pufereq/simulat/commit/e34302db8b882c5359bc33bcb75d9e083ac2ae69) **view**: add menu support for main menu
- [`ecc34b2`](https://github.com/pufereq/simulat/commit/ecc34b22acfc910460721a384d32e598927944fa) **ui**: add menu handler

### Miscellaneous Tasks

- [`6b2bff8`](https://github.com/pufereq/simulat/commit/6b2bff8f1901973303b7a5719384da0de85f8960) **CHANGELOG.md**: bump version
- [`aa443a5`](https://github.com/pufereq/simulat/commit/aa443a5f841e98413bc8412a534098e76f36455d) implement error handler
- [`63b0fb4`](https://github.com/pufereq/simulat/commit/63b0fb4f15f3e94150cd340c820dc0172379bf6a) **init**: change init order
- [`e546a77`](https://github.com/pufereq/simulat/commit/e546a77b0b5c9cc3bc5d9ea6b164de57b5348d9b) implement `info` key to main menu

### Refactor

- [`a6ad9fc`](https://github.com/pufereq/simulat/commit/a6ad9fc42a457f459241a176820b9ce3ea55d7d1) remove need for using keys when not needed in menu handler

### Styling

- [`9caaed3`](https://github.com/pufereq/simulat/commit/9caaed35bf49000ab519dfc289e8f6665f2fbdf2) **menu.py**: add types to variable names to improve readability
- [`a23e9bc`](https://github.com/pufereq/simulat/commit/a23e9bc19131d29dce116d1ba92f2e78ac8e72f3) clean up leftover comments and make code more readable

## [0.1.0-dev.1] - 2023-03-17

### Documentation

- [`a728fd8`](https://github.com/pufereq/simulat/commit/a728fd8d509d95022236777c8f8da68d3bd7d6ac) add .gitignore
- [`e666deb`](https://github.com/pufereq/simulat/commit/e666debdb4cffd3c0df509a7b440af57b1880280) add CODE_OF_CONDUCT.md
- [`53394a0`](https://github.com/pufereq/simulat/commit/53394a014fd0c4afe8c0092051a5daf373cd2882) add CONTRIBUTING.md
- [`dd27dfc`](https://github.com/pufereq/simulat/commit/dd27dfcaa6bc63a742756523f0e28518ad600aee) **readme**: add README.md
- [`fc64e79`](https://github.com/pufereq/simulat/commit/fc64e79918d00b151abc9c8f39b418b5ec88f55f) add LICENSE

### Features

- [`eb52767`](https://github.com/pufereq/simulat/commit/eb5276777f6e421ccfde24a676c0f73aabb5be15) add main.py
- [`0ca7379`](https://github.com/pufereq/simulat/commit/0ca73798c25f30a15eeaf6bbb1165d0e60fb2fe1) **init**: add init.py
- [`7126eef`](https://github.com/pufereq/simulat/commit/7126eef170c92c7a253dded1359f5aad6d16f8d6) **ui**: add topbar

### Build

- [`11cd1e4`](https://github.com/pufereq/simulat/commit/11cd1e4cbc7e1655d6b4739620f8206d7c473c86) add .vscode

<!-- generated by git-cliff -->

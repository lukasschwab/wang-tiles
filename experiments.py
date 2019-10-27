import importlib, os, random
import tiles, uni, svg

# REPL shortcut: lazy exit.
x = exit

# Default number of rows and columns for grids.
def_rows, def_cols = 10, 10

# fill produces a grid that'll unicode-print to the size of the terminal.
#
# F is some function that takes the named arguments ROWS (int), COLS (int); most
# of the grid-generating functions here conform to that interface.
#
# e.g. `fill(full_grid)`
def fill(f):
    global def_rows, def_cols
    # Get dimensions of the open terminal.
    term_rows, term_cols = os.popen('stty size', 'r').read().split()
    return f(rows=int(term_rows), cols=int(term_cols))

# random_tile is a shortcut for constructing a random Tile.
def random_tile():
    return tiles.Tile(tiles.COLORS)

# full_grid returns a grid filled with randomly selected tiles.
def full_grid(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            tile = random_tile()
            while not grid.insert(tile, row, col):
                tile = random_tile()
    return grid

# full_minimal_grid prefers previously-seen tiles to random new tiles.
def full_minimal_grid(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    known = set([random_tile()])
    for row in range(rows):
        for col in range(cols):
            for tile in known:
                if grid.insert(tile, row, col):
                    break
            else:
                while not grid.insert(tile, row, col):
                    tile = random_tile()
                known.add(tile)
    print("Used this many tiles:", len(known))
    return grid

# full_unicodable_grid returns a grid with dimensions ROWS, COLS that is filled
# with only unicode-mapped tiles (according to the mapping in uni.py).
# Following the 'minimal' pattern helps to avoid deadlock; so does limiting to
# the set of simple (non-strong, non-double) tiles.
def full_unicodable_grid(rows=def_rows, cols=def_cols, simple=False):
    f = uni.maps_to_simple_token if simple else uni.maps_to_token
    grid = tiles.Grid(rows, cols)
    known = set([random_tile()])
    for row in range(rows):
        for col in range(cols):
            for tile in known:
                if f(tile) and grid.insert(tile, row, col):
                    break
            else:
                while not f(tile) or not grid.insert(tile, row, col):
                    tile = random_tile()
                known.add(tile)
    print("Used this many tiles:", len(known))
    return grid

# key_to_tile converts a letter key (like those used in uni.py) into a
# corresponding Tile.
#
# TODO: this really belongs in uni.py with the other conversion utilities; for
# now it's only here to prevent circular imports.
def key_to_tile(key):
    assert len(key) is 4
    t = random_tile()
    dirs = ["north", "east", "south", "west"]
    t.north = uni.letter_to_color[key[0]]
    t.east = uni.letter_to_color[key[1]]
    t.south = uni.letter_to_color[key[2]]
    t.west = uni.letter_to_color[key[3]]
    return t

# WALL_KEYS is a list of uni.py-style string keys that correspond to unicode
# box-drawing characters that only use weak lines.
WALL_KEYS = [
    "WWWW",                                         # 4-0
    "WWWN", "WWNW", "WNWW", "NWWW",                 # 3-1
    "WWNN", "WNWN", "WNNW", "NWWN", "NWNW", "NNWW", # 2-2
    "NNNW", "NNWN", "NWNN", "WNNN",                 # 1-3
    "NNNN"                                          # 0-4
]

# WALL_TILES is the list of tiles corresponding to WALL_KEYS.
WALL_TILES = [key_to_tile(key) for key in WALL_KEYS]

# full_wall_grid returns a filled grid that only uses the tiles in WALL_TILES.
def full_wall_grid(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            random.shuffle(WALL_TILES)
            for tile in WALL_TILES:
                if grid.insert(tile, row, col):
                    break
            else:
                print("Error: couldn't get a suitable tile.")
                # Return the partially-filled grid.
                return grid
    return grid

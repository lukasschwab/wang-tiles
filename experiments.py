# REPL shortcuts
import importlib, os

def rl():
    importlib.reload(tiles)
    print("Reloaded tiles.py")

def x():
    exit()

# Default number of rows and columns for grids.
def_rows, def_cols = 10, 10

# fill produces a grid that'll unicode-print to the size of the terminal.
# F is some function that takes the named arguments ROWS (int), COLS (int); most
# of the grid-generating functions here conform to that interface.
def fill(f):
    global def_rows, def_cols
    # Get dimensions of the open terminal.
    term_rows, term_cols = os.popen('stty size', 'r').read().split()
    return f(rows=int(term_rows), cols=int(term_cols))

# Experiments
import tiles, uni, random

def randomTile():
    return tiles.Tile(tiles.colors)

# fullGrid returns a grid filled with randomly selected tiles.
def fullGrid(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            tile = randomTile()
            while not grid.insert(tile, row, col):
                tile = randomTile()
    return grid

# fullGridMinimal prefers previously-seen tiles to random new tiles.
def fullGridMinimal(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    known = set([randomTile()])
    for row in range(rows):
        for col in range(cols):
            for tile in known:
                if grid.insert(tile, row, col):
                    break
            else:
                while not grid.insert(tile, row, col):
                    tile = randomTile()
                known.add(tile)
    print("Used this many tiles:", len(known))
    return grid

# fullUnicodableGrid returns a grid with dimensions ROWS, COLS that is filled
# with only unicode-mapped tiles (according to the mapping in uni.py).
# Following the 'minimal' pattern helps to avoid deadlock; so does limiting to
# the set of simple (non-strong, non-double) tiles.
def fullUnicodableGrid(rows=def_rows, cols=def_cols, simple=False):
    f = uni.maps_to_simple_token if simple else uni.maps_to_token
    grid = tiles.Grid(rows, cols)
    known = set([randomTile()])
    for row in range(rows):
        for col in range(cols):
            for tile in known:
                if f(tile) and grid.insert(tile, row, col):
                    break
            else:
                while not f(tile) or not grid.insert(tile, row, col):
                    tile = randomTile()
                known.add(tile)
    print("Used this many tiles:", len(known))
    return grid

def keyToTile(key):
    assert len(key) is 4
    t = tiles.Tile(tiles.colors)
    dirs = ["north", "east", "south", "west"]
    t.north = uni.letter_to_color[key[0]]
    t.east = uni.letter_to_color[key[1]]
    t.south = uni.letter_to_color[key[2]]
    t.west = uni.letter_to_color[key[3]]
    return t

wallKeys = ["WWWW", "WWWN", "WWNW", "WNWW", "NWWW", "WWNN", "WNWN", "WNNW", "NWWN", "NWNW", "NNWW", "NNNW", "NNWN", "NWNN", "WNNN", "NNNN", "NNNN"]
wallTiles = [keyToTile(key) for key in wallKeys]

def fullWallGrid(rows=def_rows, cols=def_cols):
    grid = tiles.Grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            random.shuffle(wallTiles)
            for tile in wallTiles:
                if grid.insert(tile, row, col):
                    break
            else:
                print("Error: couldn't get a suitable tile.")
                return grid
    return grid

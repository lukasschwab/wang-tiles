# REPL shortcuts
import importlib

def rl():
    importlib.reload(tiles)
    print("Reloaded tiles.py")

def x():
    exit()

# Experiments
import tiles, uni, random

def randomTile():
    return tiles.Tile(tiles.colors)

# fillSquare returns a grid filled with randomly selected tiles.
def fillSquare(rows=10, cols=10):
    grid = tiles.Grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            tile = randomTile()
            while not grid.insert(tile, row, col):
                tile = randomTile()
    return grid

# fillSquareMinimal prefers previously-seen tiles to random new tiles.
def fillSquareMinimal(rows=10, cols=10):
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

# fillUnicodableSquare returns a grid with dimensions ROWS, COLS that is filled
# with only unicode-mapped tiles (according to the mapping in uni.py).
# Following the 'minimal' pattern helps to avoid deadlock; so does limiting to
# the set of simple (non-strong, non-double) tiles.
def fillUnicodableSquare(rows=10, cols=10, simple=False):
    f = uni.mapsToSimpleToken if simple else uni.mapsToToken
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

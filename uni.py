import random

# This file contains an extended experiment: to produce grids of Wang tiles that
# can be represented with unicode box-drawing characters. Ideally, these would
# look something like continuous, interesting terrains; so far, they do not.
#
# This file uses an unfortunate internal convention: it was easier to use
# letters as a mnemonic for the kinds of connections the box-drawing characters
# offer than to use the "color" numbers in tiles.py. This file contains a
# number of utilities for converting between those formats.
#
# "N": no line to this edge.
# "W": weak line in this direction.
# "S": strong line in this direction.
# "D": double-line in this direction.

# color_to_letter provides a mapping between tiles.py "color"-designators (ints)
# and the letters used to denote unicode line quality here.
color_to_letter = {
    1: "W", # Weak
    2: "S", # Strong
    3: "D", # Double
    4: "N", # None
}

# letter_to_color provides the inverse of the mapping in color_to_letter.
letter_to_color = dict(zip(color_to_letter.values(), color_to_letter.keys()))

# tokens provides a mapping between a tile's edge-configuration and a string
# containing the unicode box-drawing characters that match that configuration.
#
# The configuration keys are given clockwise starting from the north:
# north, east, west, south.
tokens = {
    "NNNN": " ",
    "NWNW": "─┄┈╌",
    "NSNS": "━┅┉╍",
    "WNWN": "│┆┊╎",
    "SNSN": "┃┇┋╏",
    "NWWN": "┌╭",
    "NSWN": "┍",
    "NWSN": "┎",
    "NSSN": "┏",
    "NNWW": "┐╮",
    "NNWS": "┑",
    "NNSW": "┒",
    "NNSS": "┓",
    "WWNN": "└╰",
    "WSNN": "┕",
    "SWNN": "┖",
    "SSNN": "┗",
    "WNNW": "┘╯",
    "WNNS": "┙",
    "SNNW": "┚",
    "SNNS": "┛",
    "WWWN": "├",
    "WSWN": "┝",
    "SWWN": "┞",
    "WWSN": "┟",
    "SWSN": "┠",
    "SSWN": "┡",
    "WSSN": "┢",
    "SSSN": "┣",
    "WNWW": "┤",
    "WNWS": "┥",
    "SNWW": "┦",
    "WNSW": "┧",
    "SNSW": "┨",
    "SNWS": "┩",
    "WNSS": "┪",
    "SNSS": "┫",
    "NWWW": "┬",
    "NWWS": "┭",
    "NSWW": "┮",
    "NSWS": "┯",
    "NWSW": "┰",
    "NWSS": "┱",
    "NSSW": "┲",
    "NSSS": "┳",
    "WWNW": "┴",
    "WWNS": "┵",
    "WSNW": "┶",
    "WSNS": "┷",
    "SWNW": "┸",
    "SWNS": "┹",
    "SSNW": "┺",
    "SSNS": "┻",
    "WWWW": "┼",
    "WWWS": "┽",
    "WSWW": "┾",
    "WSWS": "┿",
    "SWWW": "╀",
    "WWSW": "╁",
    "SWSW": "╂",
    "SWWS": "╃",
    "SSWW": "╄",
    "WWSS": "╅",
    "WSSW": "╆",
    "SSWS": "╇",
    "WSSS": "╈",
    "SWSS": "╉",
    "SSSW": "╊",
    "SSSS": "╋",
    "NDND": "═",
    "DNDN": "║",
    "NDWN": "╒",
    "NWDN": "╓",
    "NDDN": "╔",
    "NNWD": "╕",
    "NNDW": "╖",
    "NNDD": "╗",
    "WDNN": "╘",
    "DWNN": "╙",
    "DDNN": "╚",
    "WNND": "╛",
    "DNNW": "╜",
    "DNND": "╝",
    "WDWN": "╞",
    "DWDN": "╟",
    "DDDN": "╠",
    "WNWD": "╡",
    "DNDW": "╢",
    "DNDD": "╣",
    "NDWD": "╤",
    "NSDS": "╥",
    "NDDD": "╦",
    "WDND": "╧",
    "DWNW": "╨",
    "DDND": "╩",
    "WDWD": "╪",
    "DWDW": "╫",
    "DDDD": "╬",
    "NNNW": "╴",
    "WNNN": "╵",
    "NWNN": "╶",
    "NNWN": "╷",
    "NNNS": "╸",
    "SNNN": "╹",
    "NSNN": "╺",
    "NNSN": "╻",
    "NSNW": "╼",
    "WNSN": "╽",
    "NWNS": "╾",
    "SNWN": "╿"
}

# _get_tokens is an internal accessor method for fetching a token from the map;
# if KEY does not correspond to at least one unicode box-drawing character, the
# empty space character ` ` is returned.
def _get_tokens(key):
    try:
        return tokens[key]
    except:
        return " "

# _get_key returns the string key corresponding to the edge configuration of
# the wang tile TILE.
def _get_key(tile):
    return "".join([color_to_letter[c] for c in [
        tile.north,
        tile.south,
        tile.east,
        tile.west
    ]])

# maps_to_token returns true iff TILE's configuration corresponds to a unicode
# box-drawing character.
def maps_to_token(tile):
    return _get_tokens(_get_key(tile)) is not " "

# maps_to_simple_token returns true iff TILE's configuration corresponds to a
# unicode box-drawing character with neither double lines nor strong lines.
#
# This is useful for preventing deadlocks, because the weak<>strong transition
# tileset and the double-lined tileset are limited.
def maps_to_simple_token(tile):
    key = _get_key(tile)
    if 'S' in key or 'D' in key:
        return False
    return _get_tokens(key) is not " "

# tile_to_token returns a unicode token corresponding to TILE's configuration.
#
# If there are multiple matching unicode characters and SIMPLEST is False, a
# random corresponding character is returned; otherwise, the first-listed
# (usually un-dotted and uncurved) character is returned.
def tile_to_token(tile, simplest=True):
    tokens = _get_tokens(_get_key(tile))
    return tokens[0] if simplest else random.choice(tokens)

# to_uni returns a unicode string representation of GRID.
def to_uni(grid, simplest=True):
    rows = ["".join([tile_to_token(t, simplest) for t in row]) for row in grid.internal]
    return u"\n".join(rows)

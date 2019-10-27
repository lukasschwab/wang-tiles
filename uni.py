import random

# This file contains an extended experiment: to use ASCII drawing

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

colorToLetter = {
    1: "W", # Weak
    2: "S", # Strong
    3: "D", # Double
    4: "N", # None
}

letterToColor = dict(zip(colorToLetter.values(), colorToLetter.keys()))

# TODO: need to restrict tiles to the set of legal unicode box tokens.

notFoundTokens = set()

def _getToken(key):
    try:
        return tokens[key]
    except:
        notFoundTokens.add(key)
        return " "

def _getKey(tile):
    return "".join([colorToLetter[c] for c in [
        tile.north,
        tile.south,
        tile.east,
        tile.west
    ]])

def mapsToToken(tile):
    return _getToken(_getKey(tile)) is not " "

def mapsToSimpleToken(tile):
    key = _getKey(tile)
    # Exclude strong and double lines: they have limited tilesets.
    if 'S' in key or 'D' in key:
        return False
    return _getToken(key) is not " "

def tileToToken(tile, simplest=True):
    s = "".join([colorToLetter[c] for c in [tile.north, tile.east, tile.south, tile.west]])
    tokens = _getToken(s)
    return tokens[0] if simplest else random.choice(tokens)

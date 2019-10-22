import random

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

# TODO: need to restrict tiles to the set of legal unicode box tokens.

notFoundTokens = set()

def _getToken(key):
    try:
        return tokens[key]
    except:
        notFoundTokens.add(key)
        return " "

def tileToToken(tile):
    s = "".join([colorToLetter[c] for c in [tile.north, tile.east, tile.south, tile.west]])
    return random.choice(_getToken(s))

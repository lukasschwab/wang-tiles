import svgwrite

# COLOR SCHEMES

# NOTE: the dictionary indices in this file must correspond to the "color"
# identifiers in tiles.py.

# high_contrast is an unappealing color scheme.
high_contrast = {
    1: "blue",
    2: "purple",
    3: "green",
    4: "yellow"
}

# wada_281 is a somewhat more appealing color scheme.
wada_281 = {
    1: "steelblue",
    2: "teal",
    3: "lemonchiffon",
    4: "lightgreen"
}

# GEOMETRY

# TILE_EDGE_LENGTH is the edge-length of a square tile in the output SVG.
TILE_EDGE_LENGTH = 20

# TILE_EDGE_MIDPOINT is one half of TILE_EDGE_LENGTH.
TILE_EDGE_MIDPOINT = TILE_EDGE_LENGTH / 2

# get_triangle_points calculates the vertices of a triangle in the output SVG
# representing the edge in direction DIRECTION of a tile at position row, col
# of a grid. It's unlikley to be a useful function outside of its use in to_svg.
#
# TODO: drawing merged squares instead of triangles when possible would nearly
# quarter the number of rendered polygons.
def get_triangle_points(row, col, direction):
    col_offset = col * TILE_EDGE_LENGTH
    row_offset = row * TILE_EDGE_LENGTH
    cases = {
        "north": [
            (col_offset + 0, row_offset + 0),
            (col_offset + TILE_EDGE_MIDPOINT, row_offset + TILE_EDGE_MIDPOINT),
            (col_offset + TILE_EDGE_LENGTH, row_offset + 0)
        ],
        "east": [
            (col_offset + TILE_EDGE_LENGTH, row_offset + 0),
            (col_offset + TILE_EDGE_MIDPOINT, row_offset + TILE_EDGE_MIDPOINT),
            (col_offset + TILE_EDGE_LENGTH, row_offset + TILE_EDGE_LENGTH)
        ],
        "south": [
            (col_offset + TILE_EDGE_LENGTH, row_offset + TILE_EDGE_LENGTH),
            (col_offset + TILE_EDGE_MIDPOINT, row_offset + TILE_EDGE_MIDPOINT),
            (col_offset + 0, row_offset + TILE_EDGE_LENGTH)
        ],
        "west": [
            (col_offset + 0, row_offset + 0),
            (col_offset + TILE_EDGE_MIDPOINT, row_offset + TILE_EDGE_MIDPOINT),
            (col_offset + 0, row_offset + TILE_EDGE_LENGTH)
        ]
    }
    return cases[direction]

# to_svg writes an SVG representation of GRID to FILENAME. CLRS must represent a
# valid color scheme: a dict mapping tiles.py "color" ints to valid SVG color
# identifiers. See e.g. high_contrast and wada_281 above.
def to_svg(grid, filename="wang.svg", clrs=wada_281):
    dwg = svgwrite.Drawing(filename, size=(str(TILE_EDGE_LENGTH * grid.cols), str(TILE_EDGE_LENGTH * grid.rows)))
    row_i = 0
    for row in grid.internal:
        col_i = 0
        for tile in row:
            dwg.add(dwg.polygon(points=get_triangle_points(row_i, col_i, "north")).fill(clrs[tile.north]))
            dwg.add(dwg.polygon(points=get_triangle_points(row_i, col_i, "east")).fill(clrs[tile.east]))
            dwg.add(dwg.polygon(points=get_triangle_points(row_i, col_i, "south")).fill(clrs[tile.south]))
            dwg.add(dwg.polygon(points=get_triangle_points(row_i, col_i, "west")).fill(clrs[tile.west]))
            col_i += 1
        row_i += 1
    dwg.save()

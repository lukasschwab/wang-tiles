# Wang tiles.

import random, svgwrite

DIRECTIONS = set(["north", "east", "south", "west"])

colors = [1,2,3,4]
svgColors = {
    1: "blue",
    2: "purple",
    3: "green",
    4: "yellow"
}
altSvgColors = {
    1: "steelblue",
    2: "teal",
    3: "lemonchiffon",
    4: "lightgreen"
}

# SVG
tileEdgeLength = 20
tileEdgeMidpoint = tileEdgeLength / 2

class Tile:
    def __init__(self, colors):
        self.north = random.choice(colors)
        self.east = random.choice(colors)
        self.south = random.choice(colors)
        self.west = random.choice(colors)

    def prettyPrint(self):
        print("", self.north)
        print(self.west, self.east)
        print("", self.south)

    def canFit(self, otherTile, direction):
        assert direction in DIRECTIONS
        if otherTile == None:
            print("Other tile is none.")
            return True
        canFitDirections = {
            "north": self.north == otherTile.south,
            "east": self.east == otherTile.west,
            "south": self.south == otherTile.north,
            "west": self.west == otherTile.east
        }
        return canFitDirections[direction]

def getTrianglePoints(row, col, direction):
    assert direction in DIRECTIONS
    col_offset = col * tileEdgeLength
    row_offset = row * tileEdgeLength
    cases = {
        "north": [
            (col_offset + 0, row_offset + 0),
            (col_offset + tileEdgeMidpoint, row_offset + tileEdgeMidpoint),
            (col_offset + tileEdgeLength, row_offset + 0)
        ],
        "east": [
            (col_offset + tileEdgeLength, row_offset + 0),
            (col_offset + tileEdgeMidpoint, row_offset + tileEdgeMidpoint),
            (col_offset + tileEdgeLength, row_offset + tileEdgeLength)
        ],
        "south": [
            (col_offset + tileEdgeLength, row_offset + tileEdgeLength),
            (col_offset + tileEdgeMidpoint, row_offset + tileEdgeMidpoint),
            (col_offset + 0, row_offset + tileEdgeLength)
        ],
        "west": [
            (col_offset + 0, row_offset + 0),
            (col_offset + tileEdgeMidpoint, row_offset + tileEdgeMidpoint),
            (col_offset + 0, row_offset + tileEdgeLength)
        ]
    }
    return cases[direction]

class Grid:
    def __init__(self, height, width):
        assert width > 0;
        assert height > 0;
        self.rows = height
        self.cols = width
        self.internal = [[ None ] * width for h in range(height)]

    def get(self, row, col):
        if not self.isInBounds(row, col):
            return None
        return self.internal[row][col]

    def isInBounds(self, row, col):
        return row >= 0 and row < len(self.internal) and col >= 0 and col < len(self.internal[0])

    def canFit(self, newTile, row, col):
        # Don't allow double-placement.
        if (self.internal[row][col] is not None):
            print("OCCUPIED")
            return False
        out = True
        toNorth = self.get(row - 1, col)
        if toNorth is not None:
            out = out and newTile.canFit(toNorth, "north")
        toEast = self.get(row, col + 1)
        if toEast is not None:
            out = out and  newTile.canFit(toEast, "east")
        toSouth = self.get(row + 1, col)
        if toSouth is not None:
            out = out and newTile.canFit(toSouth, "south")
        toWest = self.get(row, col - 1)
        if toWest is not None:
            out = out and newTile.canFit(toWest, "west")
        return out

    def insert(self, newTile, row, col):
        assert self.isInBounds(row, col)
        if not self.canFit(newTile, row, col):
            return False
        self.internal[row][col] = newTile
        return True

    def prettyPrint(self):
        for row in self.internal:
            # Print north directions.
            norths = []
            for elem in row:
                if elem is not None:
                    norths.append(str(elem.north))
                else:
                    norths.append("•")
            print("", "  ".join(norths), "")
            # Print east/west directions.
            eastsAndWests = []
            for elem in row:
                if elem is not None:
                    eastsAndWests.append(str(elem.west) + " " + str(elem.east))
                else:
                    eastsAndWests.append("• •")
            print("".join(eastsAndWests))
            souths = []
            for elem in row:
                if elem is not None:
                    souths.append(str(elem.south))
                else:
                    souths.append("•")
            print("", "  ".join(souths), "")

    def toSVG(self, filename="wang.svg", clrs=svgColors):
        dwg = svgwrite.Drawing(filename)
        row_i = 0
        for row in self.internal:
            col_i = 0
            for tile in row:
                dwg.add(dwg.polygon(points=getTrianglePoints(row_i, col_i, "north")).fill(clrs[tile.north]))
                dwg.add(dwg.polygon(points=getTrianglePoints(row_i, col_i, "east")).fill(clrs[tile.east]))
                dwg.add(dwg.polygon(points=getTrianglePoints(row_i, col_i, "south")).fill(clrs[tile.south]))
                dwg.add(dwg.polygon(points=getTrianglePoints(row_i, col_i, "west")).fill(clrs[tile.west]))
                col_i += 1
            row_i += 1
        dwg.save()

    def toUni(self):
        import uni
        for row in self.internal:
            print("".join([uni.tileToToken(t) for t in row]))

# dwg = svgwrite.Drawing('wang.svg', profile='tiny')
# dwg.add(dwg.polygon(points=[(0,0), (10,10), (20,0)]).fill("blue"))
# dwg.save()

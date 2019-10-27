import random
import svg, uni

# COLORS are a schema of unspecified colors. To add more colors, extend the list
# here and ensure that the dicts in svg.py and uni.py are updated to contain
# all additional color keys.
COLORS = [1,2,3,4]

# Class Tile represents a single Wang tile with four sides that can be assembled
# into a Grid of Wang tiles.
class Tile:
    # Construct a new Tile with edges randomly selected from COLORS.
    def __init__(self, colors):
        self.north = random.choice(colors)
        self.east = random.choice(colors)
        self.south = random.choice(colors)
        self.west = random.choice(colors)

    # pretty_print produces a diamond-shaped numerical representation of this
    # Tile identical to its representation in a Grid.pretty_print output.
    def pretty_print(self):
        print("", self.north)
        print(self.west, self.east)
        print("", self.south)

    # can_fit returns true iff OTHERTILE can be placed adjacent to this Tile in
    # direction DIRECTION.
    #
    # e.g. suppose direction="north", otherTile.south=1, and self.north=1. Then
    # can_fit(self, otherTile, direction) will return True.
    def can_fit(self, otherTile, direction):
        assert direction in set(["north", "east", "south", "west"])
        if otherTile == None:
            return True
        canFitDirections = {
            "north": self.north == otherTile.south,
            "east": self.east == otherTile.west,
            "south": self.south == otherTile.north,
            "west": self.west == otherTile.east
        }
        return canFitDirections[direction]

# Class Grid represents a mutable grid of None-able Wang tiles with a fixed
# dimension.
class Grid:
    # Construct a new empty (None-filled) grid with dimensions HEIGHT, WIDTH.
    def __init__(self, height, width):
        assert width > 0;
        assert height > 0;
        self.rows = height
        self.cols = width
        self.internal = [[ None ] * width for h in range(height)]

    # get returns the Tile (None-able) at position row, col in this Grid.
    def get(self, row, col):
        if not self.is_in_bounds(row, col):
            return None
        return self.internal[row][col]

    # is_in_bounds returns True iff the position row, col is a valid position in
    # this grid.
    def is_in_bounds(self, row, col):
        return row >= 0 and row < len(self.internal) and col >= 0 and col < len(self.internal[0])

    # can_fit returns True iff NEWTILE can be placed at position row, col in
    # this Grid, i.e. the position is unoccupied (None) and the Wang tile rule
    # (that adjacent edges must match colors) would not be violated by this
    # placement.
    def can_fit(self, newTile, row, col):
        # Don't allow double-placement.
        if (self.internal[row][col] is not None):
            print("OCCUPIED")
            return False
        out = True
        toNorth = self.get(row - 1, col)
        out = out and newTile.can_fit(toNorth, "north")
        toEast = self.get(row, col + 1)
        out = out and  newTile.can_fit(toEast, "east")
        toSouth = self.get(row + 1, col)
        out = out and newTile.can_fit(toSouth, "south")
        toWest = self.get(row, col - 1)
        out = out and newTile.can_fit(toWest, "west")
        return out

    # insert attempts to insert NEWTILE at position row, col in this Grid and
    # returns True iff the insertion succeeded (i.e. the grid is updated).
    def insert(self, newTile, row, col):
        assert self.is_in_bounds(row, col)
        if not self.can_fit(newTile, row, col):
            return False
        self.internal[row][col] = newTile
        return True

    # pretty_print returns a numberic representation of the numbered edge-
    # adjacencies in this Grid. This representation is actually not very pretty
    # compared to the SVG output produced by to_svg.
    def pretty_print(self):
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

    # to_svg writes a default SVG representation of this Grid to file.
    def to_svg(self):
        return svg.to_svg(self)

    # to_uni prints and returns a unicode representation of this grid. Note: the
    # tiles in this grid are not guaranteed to map to unicode box-drawing
    # characters unless this property has been confirmed upon insertion.
    def to_uni(self):
        out = uni.to_uni(self)
        print(out)
        return out

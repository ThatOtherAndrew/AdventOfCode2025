from itertools import combinations

type Point = tuple[int, int]
type Rect = tuple[Point, Point]


def rectangles_intersect(r1: Rect, r2: Rect) -> bool:
    # hypothesis: two rects intersect iff both their x-ranges and y-ranges intersect

    # shuffle rects into intervals from lower to higher x and y values
    (r1_x_lower, r1_x_upper), (r1_y_lower, r1_y_upper) = sorted((r1[0][0], r1[1][0])), sorted((r1[0][1], r1[1][1]))
    (r2_x_lower, r2_x_upper), (r2_y_lower, r2_y_upper) = sorted((r2[0][0], r2[1][0])), sorted((r2[0][1], r2[1][1]))

    # test if x- and y-ranges intersect
    return (
        max(r1_x_lower, r2_x_lower) <= min(r1_x_upper, r2_x_upper)  # x-ranges
        and max(r1_y_lower, r2_y_lower) <= min(r1_y_upper, r2_y_upper)  # y-ranges
    )


def main():
    # noinspection PyTypeChecker
    tiles: list[Point] = [tuple(map(int, line.split(','))) for line in open('.input.txt')]

    # firstly, let's find all the turns needed to trace the polygon, and the inner and outer cells
    turns: list[int] = []
    cells: list[tuple[Point, Point]] = []
    for a, b, c in zip(tiles, tiles[1:] + tiles[:1], tiles[2:] + tiles[:2]):
        # compute b->a and b->c normalised to length 1
        v1 = ((a[0] - b[0]) // (abs(a[0] - b[0]) or 1), (a[1] - b[1]) // (abs(a[1] - b[1]) or 1))
        v2 = ((c[0] - b[0]) // (abs(c[0] - b[0]) or 1), (c[1] - b[1]) // (abs(c[1] - b[1]) or 1))
        # calculate cross product (ad - bc) to get direction (left turn or right turn)
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]

        # find the cell nestled in the corner of the angle
        inner_cell = (b[0] + v1[0] + v2[0], b[1] + v1[1] + v2[1])
        # find the cell poked by the pointy corner of the angle
        outer_cell = (b[0] - v1[0] - v2[0], b[1] - v1[1] - v2[1])

        turns.append(int(cross_product < 0))  # 0 = L, 1 = R
        cells.append((inner_cell, outer_cell))

    # next, let's join up all cells exterior to the polygon, to get an outer "wrapping" polygon
    # (we're assuming the polygon was traced clockwise for convenience)
    wrapping_corners: list[Point] = [cell[turn] for turn, cell in zip(turns, cells)]
    wrapping_sides: list[Rect] = list(zip(wrapping_corners, wrapping_corners[1:] + wrapping_corners[:1]))

    # lastly, get all rectangle sizes just like part 1, but filter out ones which intersect any wrapping sides
    sizes = [
        (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        for a, b in combinations(tiles, 2)
        if not any(rectangles_intersect(side, (a, b)) for side in wrapping_sides)
    ]

    print(max(sizes))


if __name__ == '__main__':
    main()

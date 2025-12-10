from itertools import combinations, chain


def main():
    tiles = [tuple(map(int, line.split(','))) for line in open('input2.txt')]

    # firstly, let's find all the cells nested in the concave angles and adjacent to the convex angles
    left_turns = []
    right_turns = []
    for a, b, c in zip(tiles, tiles[1:] + tiles[:1], tiles[2:] + tiles[:2]):
        # compute b->a and b->c normalised to length 1
        v1 = ((a[0] - b[0]) // (abs(a[0] - b[0]) or 1), (a[1] - b[1]) // (abs(a[1] - b[1]) or 1))
        v2 = ((c[0] - b[0]) // (abs(c[0] - b[0]) or 1), (c[1] - b[1]) // (abs(c[1] - b[1]) or 1))
        # calculate cross product (ad - bc) to get direction (left turn or right turn)
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]

        # find the cell nestled in the corner of the angle
        inner_cell = (b[0] + v1[0] + v2[0], b[1] + v1[1] + v2[1])
        # find the two cells adjacent to the angle sides
        outer_cells = ((b[0] - v1[0] - v2[0], b[1]), (b[0], b[1] - v1[1] - v2[1]))

        (left_turns if cross_product > 0 else right_turns).append((inner_cell, *outer_cells))

    # now, one list is shorter than the other by 4 items, because there are 4 more convex than concave corners
    concave_points, convex_points = sorted((left_turns, right_turns), key=len)
    # let's use this new info to create a new array of all bad points
    bad_points = list(chain(*(t[:1] for t in concave_points), *(t[1:] for t in convex_points)))

    # lastly, get all rectangle sizes just like part 1, but filter out ones which contain bad points
    sizes = [
        (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        for a, b in combinations(tiles, 2)
        if not any(
            (
                min(a[0], b[0]) <= point[0] <= max(a[0], b[0])
                and min(a[1], b[1]) <= point[1] <= max(a[1], b[1])
            )
            for point in bad_points
        )
    ]

    print(max(sizes))


if __name__ == '__main__':
    main()

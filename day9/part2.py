from itertools import combinations


def main():
    tiles = [tuple(map(int, line.split(','))) for line in open('input.txt')]

    # firstly, let's find all the cells nested in the concave angles
    left_turns = []
    right_turns = []
    for a, b, c in zip(tiles, tiles[1:] + tiles[:1], tiles[2:] + tiles[:2]):
        # compute b->a x b->c to get direction (left turn or right turn)
        v1 = (a[0] - b[0], a[1] - b[1])
        v2 = (c[0] - b[0], c[1] - b[1])
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]  # ad - bc

        # find the cell nestled in the corner of the angle
        cell = (b[0] + (-1, 1)[v1[0] + v2[0] > 0], b[1] + (-1, 1)[v1[1] + v2[1] > 0])
        (left_turns if cross_product > 0 else right_turns).append(cell)

    # now, one list is shorter than the other by 4 items - discard the larger one
    concave_points = min(left_turns, right_turns, key=len)

    # lastly, get all rectangle sizes just like part 1, but filter out ones which contain concave points
    sizes = [
        (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        for a, b in combinations(tiles, 2)
        if not any(
            (
                min(a[0], b[0]) <= point[0] <= max(a[0], b[0])
                and min(a[1], b[1]) <= point[1] <= max(a[1], b[1])
            )
            for point in concave_points
        )
    ]

    print(max(sizes))


if __name__ == '__main__':
    main()

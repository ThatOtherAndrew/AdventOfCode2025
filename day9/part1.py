from itertools import combinations


def main():
    tiles = [tuple(map(int, line.split(','))) for line in open('input.txt')]
    sizes = [(abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1) for a, b in combinations(tiles, 2)]
    print(max(sizes))


if __name__ == '__main__':
    main()

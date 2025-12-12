import re


def main():
    *pieces, all_regions = open('.input.txt').read().split('\n\n')
    areas = [piece.count('#') for piece in pieces]
    regions = [tuple(map(int, re.findall(r'\d+', line))) for line in all_regions.splitlines()]
    print(sum(
        1 for r in regions
        if r[0] * r[1] > sum(areas[i] * n for i, n in enumerate(r[2:]))
    ))


if __name__ == '__main__':
    main()

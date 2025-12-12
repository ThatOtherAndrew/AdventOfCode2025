import re


def main():
    regions = [
        tuple(map(int, re.findall(r'\d+', line)))
        for line in open('.input.txt').read().rsplit('\n\n', 1)[1].splitlines()
    ]

    print(sum(
        x * y > sum(n) * 7
        for x, y, *n in regions
    ))


if __name__ == '__main__':
    main()

import functools

import portion


def main():
    upper, lower = open('input.txt').read().split('\n\n')
    ranges = [portion.closed(int(line.split('-')[0]), int(line.split('-')[1])) for line in upper.splitlines()]

    fresh = functools.reduce(lambda a, b: a | b, ranges)
    print(fresh)
    print(sum(r.upper - r.lower + 1 for r in fresh))



if __name__ == '__main__':
    main()

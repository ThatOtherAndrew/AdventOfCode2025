import portion


def main():
    upper, lower = open('input.txt').read().split('\n\n')
    fresh_ranges = portion.empty()
    for line in upper.splitlines():
        # union of ranges handles merging of overlapping & adjacent ranges
        fresh_ranges |= portion.closed(*map(int, line.split('-')))

    print(sum(
        section.upper - section.lower + 1  # +1 to count upper/lower bounds inclusively
        for section in fresh_ranges
    ))


if __name__ == '__main__':
    main()

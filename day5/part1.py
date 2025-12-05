def main():
    upper, lower = open('input.txt').read().split('\n\n')
    ranges = [range(int(line.split('-')[0]), int(line.split('-')[1]) + 1) for line in upper.splitlines()]
    ingredients = list(map(int, lower.split()))
    print(sum(map(lambda n: any(n in r for r in ranges), ingredients)))


if __name__ == '__main__':
    main()

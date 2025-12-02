import re


def main():
    id_ranges = [tuple(map(int, s.split('-'))) for s in open('input.txt').read().split(',')]
    invalid_id_sum = 0
    # okay so it turns out that bruteforce was the way after all actually
    for start, end in id_ranges:
        for i in range(start, end + 1):
            # regex backreferences are overpowered
            if re.match(r'^(\d+)\1+$', str(i)):
                invalid_id_sum += i

    print(invalid_id_sum)


if __name__ == '__main__':
    main()

def main():
    id_ranges = [tuple(map(int, s.split('-'))) for s in open('input.txt').read().split(',')]
    invalid_id_sum = 0
    # dumb bruteforce again...
    for start, end in id_ranges:
        for i in range(start, end + 1):
            id_string = str(i)
            halfway = len(id_string) // 2
            if id_string[:halfway] == id_string[halfway:]:
                invalid_id_sum += i

    print(invalid_id_sum)


if __name__ == '__main__':
    main()

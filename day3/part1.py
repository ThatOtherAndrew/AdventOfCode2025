def main():
    banks = [list(map(int, line.strip())) for line in open('input.txt')]
    joltage_sum = 0
    for bank in banks:
        first_digit = max(bank[:-1])
        first_digit_index = bank.index(first_digit)
        last_digit = max(bank[first_digit_index+1:])
        joltage_sum += 10 * first_digit + last_digit
    print(joltage_sum)


if __name__ == '__main__':
    main()

DIGITS = 12


def main():
    banks = [list(map(int, line.strip())) for line in open('.input.txt')]
    joltage_sum = 0

    # finally, my first actually intelligent puzzle solve
    for bank in banks:
        joltage = 0
        last_digit_index = -1

        for n in range(DIGITS):
            bank_slice = slice(last_digit_index + 1, len(bank) - (DIGITS - n - 1))
            nth_digit = max(bank[bank_slice])
            last_digit_index = bank.index(nth_digit, bank_slice.start, bank_slice.stop)
            # print(last_digit_index, end=' ')
            joltage += (10 ** (DIGITS - n - 1)) * nth_digit

        joltage_sum += joltage
        # print(joltage)

    print(joltage_sum)


if __name__ == '__main__':
    main()

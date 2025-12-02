def main():
    lines = open('input.txt').readlines()
    pos = 50
    zero_count = 0
    for line in lines:
        # yes, this is a terrifically stupid implementation.
        # but it was fast to write
        if line.startswith('L'):
            for _ in range(int(line[1:])):
                pos -= 1
                pos %= 100
                if pos == 0:
                    zero_count += 1
        else:
            for _ in range(int(line[1:])):
                pos += 1
                pos %= 100
                if pos == 0:
                    zero_count += 1
    print(zero_count)


if __name__ == '__main__':
    main()

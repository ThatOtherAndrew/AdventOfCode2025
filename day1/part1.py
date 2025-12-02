def main():
    lines = open('input.txt').readlines()
    pos = 50
    zero_count = 0
    for line in lines:
        if line.startswith('L'):
            pos -= int(line[1:])
        else:
            pos += int(line[1:])
        pos %= 100
        if pos == 0:
            zero_count += 1
    print(zero_count)


if __name__ == '__main__':
    main()

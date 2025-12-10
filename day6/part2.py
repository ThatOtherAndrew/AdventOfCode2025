def main():
    raw_lines = open('input.txt').readlines()
    total = 0
    buffer = []

    for column in reversed(list(zip(*raw_lines))):
        joined = ''.join(column).strip()
        if not joined:
            continue  # skip blank columns

        buffer.append(joined)
        if joined[-1] in '+*': # last character is operator -> compute maths
            expression = buffer[-1][-1].join(buffer)[:-1]
            total += eval(expression)
            buffer = []

    print(total)

if __name__ == '__main__':
    main()

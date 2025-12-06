def main():
    maths = [line.split() for line in open('input.txt')]
    total = 0
    for terms in zip(*maths):
        expression = terms[-1].join(terms[:-1])
        total += eval(expression)
    print(total)

if __name__ == '__main__':
    main()

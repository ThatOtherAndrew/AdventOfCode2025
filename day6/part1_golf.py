print(sum(eval(t[-1].join(t[:-1]))for t in zip(*map(str.split,open('input.txt')))))

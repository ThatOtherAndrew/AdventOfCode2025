from itertools import product

from sympy import symbols, linsolve, Tuple
from tqdm import tqdm


def main():
    total_presses = 0

    for i, line in enumerate(open('input2.txt')):
        *buttons, target = [tuple(map(int, part[1:-1].split(','))) for part in line.split()[1:]]
        print(f'[{i + 1}] Solving {target}: [{"] [".join(" ".join(map(str, b)) for b in buttons)}]')

        # construct equations and simplify (basically just gaussian elimination lol)
        equations = [
            sum(symbols(f'x{a}') for a, b in enumerate(buttons) if i in b) - n
            for i, n in enumerate(target)
        ]
        solution: Tuple = next(iter(linsolve(equations, symbols(f'x0:{len(buttons)}'))))
        print(solution.free_symbols, solution)

        # test out all integer values and find the least presses for a valid solution
        min_presses = float('inf')
        depth = max(target)
        iterations = depth ** len(solution.free_symbols)
        for values in tqdm(product(*(range(depth + 1) for _ in solution.free_symbols)), total=iterations):
            substituted = solution.subs(zip(solution.free_symbols, values), simultaneous=True)
            if all(x >= 0 and x.is_integer for x in substituted):
                min_presses = min(min_presses, sum(substituted))

        total_presses += min_presses
        print('Solved:', min_presses, end='\n\n')

    print('Total:', total_presses)


if __name__ == '__main__':
    main()

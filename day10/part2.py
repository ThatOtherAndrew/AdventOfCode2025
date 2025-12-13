import math
from concurrent.futures.process import ProcessPoolExecutor
from functools import partial
from itertools import product

from sympy import symbols, linsolve, Tuple, solve
from tqdm import tqdm


def count_presses(values, solution, free_symbols):
    substituted = solution.subs(zip(free_symbols, values), simultaneous=True)
    if all(x >= 0 and x.is_integer for x in substituted):
        return sum(substituted)
    return float('inf')


def main():
    total_presses = 0

    for i, line in enumerate(open('.input.txt')):
        *buttons, target = [tuple(map(int, part[1:-1].split(','))) for part in line.split()[1:]]
        print(f'[{i + 1}] Solving {target}: [{"] [".join(" ".join(map(str, b)) for b in buttons)}]')

        # construct equations and simplify (basically just gaussian elimination lol)
        equations = [
            sum(symbols(f'x{a}') for a, b in enumerate(buttons) if i in b) - n
            for i, n in enumerate(target)
        ]
        solution: Tuple = next(iter(linsolve(equations, symbols(f'x0:{len(buttons)}'))))
        print(solution.free_symbols, solution)

        # create a search space and narrow it down to make the runtime feasible
        ranges = {
            symbol: range(max(target[i] for i in buttons[solution.index(symbol)]) + 1)
            for symbol in solution.free_symbols
        }
        for part in solution:
            if len(part.free_symbols) == 1 and not part.is_symbol:
                symbol = next(iter(part.free_symbols))
                threshold = solve(part, symbol)[0]
                if part.coeff(symbol) > 0:
                    # as symbol increases, value will increase
                    ranges[symbol] = range(max(ranges[symbol].start, math.ceil(threshold)), ranges[symbol].stop + 1)
                    print(symbol, '>=', threshold)
                else:
                    # as symbol increases, value will decrease
                    ranges[symbol] = range(ranges[symbol].start, min(ranges[symbol].stop, math.floor(threshold)) + 1)
                    print(symbol, '<=', threshold)

        # find the minimum presses out of the valid solutions in the search space
        search_space = list(product(*ranges.values()))
        with ProcessPoolExecutor() as executor:
            worker = partial(count_presses, solution=solution, free_symbols=list(ranges.keys()))
            min_presses = min(tqdm(executor.map(worker, search_space), total=len(search_space)))

        # add solution to total
        total_presses += min_presses
        print('Solved:', min_presses, end='\n\n')

    print('Total:', total_presses)


if __name__ == '__main__':
    main()

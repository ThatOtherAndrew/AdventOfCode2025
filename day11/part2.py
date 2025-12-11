import math
from collections import defaultdict
from functools import cache
from itertools import permutations, pairwise


def main():
    # reverse graph of outputs -> inputs
    graph = defaultdict(list)
    for line in open('input2.txt'):
        for output in line[5:].split():
            graph[output].append(line[:3])

    @cache
    def count_paths(root: str, node: str, via: tuple[int] = ()) -> int:
        if via:
            return sum(
                math.prod(
                    count_paths(*pair)
                    for pair in pairwise((root, *order, node))
                )
                for order in permutations(via)
            )

        if node == root:
            return 1
        return sum(count_paths(root, source) for source in graph[node])

    print(count_paths('svr', 'out', via=('fft', 'dac')))


if __name__ == '__main__':
    main()

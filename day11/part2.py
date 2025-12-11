from collections import defaultdict
from functools import cache


def main():
    # reverse graph of outputs -> inputs
    graph = defaultdict(list)
    for line in open('input2.txt'):
        for output in line[5:].split():
            graph[output].append(line[:3])

    @cache
    def count_paths(root: str, node: str) -> int:
        if node == root:
            return 1
        return sum(count_paths(root, source) for source in graph[node])

    print(
        count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
        + count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')
    )


if __name__ == '__main__':
    main()

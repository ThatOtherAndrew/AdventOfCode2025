from collections import defaultdict
from functools import cache


def main():
    # reverse graph of outputs -> inputs
    graph = defaultdict(list)
    for line in open('.input.txt'):
        for output in line[5:].split():
            graph[output].append(line[:3])

    @cache
    def count_paths_to(node: str) -> int:
        if node == 'you':
            return 1
        return sum(map(count_paths_to, graph[node]))

    print(count_paths_to('out'))


if __name__ == '__main__':
    main()

from collections import defaultdict
from collections.abc import Generator, Iterable
from functools import cache
from itertools import islice


@cache
def coin_change(target: int, coins: tuple[int], max_coins: int) -> list[list[int]]:
    if target == max_coins == 0:
        return [[0 for _ in coins]]
    if not coins:
        return []

    splits = []
    for count in range(min(target // coins[0], max_coins) + 1):
        for counts in coin_change(target - count * coins[0], coins[1:], max_coins - count):
            splits.append([count, *counts])
    return splits


def sorted_coin_change(target: int, coins: Iterable[int]) -> Generator[list[int]]:
    sorted_coins = tuple(sorted(coins, reverse=True))
    for max_coins in range(target // min(sorted_coins) + 1):
        # print(str(max_coins), end='\r')
        yield from coin_change(target, sorted_coins, max_coins)


def main():
    machines: list[tuple[list[int], dict[int, list[tuple[int, ...]]]]] = []
    for line in open('.input.txt'):
        *buttons, state = [list(map(int, part[1:-1].split(','))) for part in line.split()[1:]]
        buttons_dict = defaultdict(list)
        for button in buttons:
            buttons_dict[len(button)].append(button)
        machines.append((state, buttons_dict))

    for state, buttons in machines:
        print(
            sum(state),
            tuple(buttons.keys()),
            [*islice(sorted_coin_change(sum(state), buttons.keys()), 100)]
        )


if __name__ == '__main__':
    main()

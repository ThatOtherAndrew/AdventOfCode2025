from collections import defaultdict
from collections.abc import Generator, Iterable
from functools import cache
from itertools import combinations, product


@cache
def coin_change(target: int, coins: tuple[int], max_coins: int) -> list[list[int]]:
    if target == max_coins == 0:
        return [[0 for _ in coins]]
    if not coins:
        return []

    coin_counts = []
    for count in range(min(target // coins[0], max_coins), -1, -1):
        for counts in coin_change(target - count * coins[0], coins[1:], max_coins - count):
            coin_counts.append([count, *counts])
    return coin_counts


def sorted_coin_change(target: int, coins: tuple[int]) -> Generator[dict[int, int]]:
    for max_coins in range(target // min(coins) + 1):
        for counts in coin_change(target, coins, max_coins):
            yield {coins[i]: count for i, count in enumerate(counts)}


@cache
def partitions(n: int, k: int):
    # https://stackoverflow.com/questions/28965734/general-bars-and-stars
    for c in combinations(range(n + k - 1), k - 1):
        yield [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]


def find_least_presses(
    buttons: dict[int, list[tuple[int, ...]]],
    sizes: tuple[int],
    button_presses: Iterable[dict[int, int]],
    starting_state: tuple[int, ...]
) -> int:
    for presses in button_presses:
        button_options = {size: list(partitions(count, len(buttons[size]))) for size, count in presses.items()}
        print(*map(len, button_options.values()))

        for choices in product(*button_options.values()):
            state = list(starting_state)
            skip = False

            for i, size_choices in enumerate(choices):
                for j, size_presses in enumerate(size_choices):
                    button = buttons[sizes[i]][j]
                    for wire in button:
                        state[wire] -= size_presses

                        # gods this is ugly
                        if state[wire] < 0:
                            skip = True
                            break
                    if skip: break
                if skip: break

            if not any(state):
                return sum(map(sum, choices))

    raise RuntimeError('no solution found')


def main():
    machines = []
    for line in open('input.txt'):
        *buttons, state = [tuple(map(int, part[1:-1].split(','))) for part in line.split()[1:]]
        buttons_dict = defaultdict(list)
        for button in sorted(buttons, key=len, reverse=True):
            buttons_dict[len(button)].append(button)
        machines.append((state, buttons_dict))

    for state, buttons in machines:
        print(state, buttons)
        sizes = tuple(buttons.keys())
        button_presses = sorted_coin_change(sum(state), sizes)
        print(find_least_presses(buttons, sizes, button_presses, state))


if __name__ == '__main__':
    main()

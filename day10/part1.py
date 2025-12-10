from itertools import chain


class Machine:
    def __init__(self, state: list[bool], target: list[bool], buttons: list[tuple[int, ...]]):
        self.state = state
        self.target = target
        self.buttons = buttons
        self.is_solved = state == target

    @staticmethod
    def from_manual_line(line: str) -> Machine:
        parts = line.split()
        target = [char == '#' for char in parts[0][1:-1]]
        buttons = [tuple(map(int, part[1:-1].split(','))) for part in parts[1:-1]]
        return Machine([False for _ in target], target, buttons)

    def get_moves(self, skip_hashes: set[int]) -> list[Machine]:
        machines = []
        for button in self.buttons:
            new_state = self.state.copy()
            for i in button:
                new_state[i] = not new_state[i]

            # use hashes to avoid moves which repeat states
            state_hash = hash(tuple(new_state))
            if state_hash in skip_hashes:
                continue
            skip_hashes.add(state_hash)

            machines.append(Machine(new_state, self.target, self.buttons))

        return machines

    def solve(self) -> int:
        steps = 0
        machines = [self]
        skip_hashes = set()
        while not any(machine.is_solved for machine in machines):
            steps += 1
            machines = list(chain.from_iterable(machine.get_moves(skip_hashes) for machine in machines))
        return steps


def main():
    machines = map(Machine.from_manual_line, open('input.txt').readlines())
    print(sum(machine.solve() for machine in machines))


if __name__ == '__main__':
    main()

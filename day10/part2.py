from itertools import chain


class Machine:
    def __init__(self, state: list[int], buttons: list[tuple[int, ...]]):
        self.state = state
        self.buttons = buttons
        self.is_solved = not any(state)

    def __repr__(self) -> str:
        return repr(self.state)

    @staticmethod
    def from_manual_line(line: str) -> Machine:
        parts = line.split()
        state = list(map(int, parts[-1][1:-1].split(',')))
        buttons = [tuple(map(int, part[1:-1].split(','))) for part in parts[1:-1]]
        return Machine(state, buttons)

    def get_moves(self, skip_hashes: set[int]) -> list[Machine]:
        machines = []

        # get the index affected by the least buttons (to keep the state tree narrow)
        _, target = min((sum(i in b for b in self.buttons), i) for i, n in enumerate(self.state) if n)

        for button in self.buttons:
            if target not in button:
                continue

            new_state = self.state.copy()
            for i in button:
                new_state[i] -= 1
            if any(n < 0 for n in new_state):
                continue  # skip invalid state

            # use hashes to avoid moves which repeat states
            state_hash = hash(tuple(new_state))
            if state_hash in skip_hashes:
                continue
            skip_hashes.add(state_hash)

            machines.append(Machine(new_state, self.buttons))

        return machines

    def solve(self) -> int:
        steps = 0
        machines = [self]
        skip_hashes = set()
        while not any(machine.is_solved for machine in machines):
            steps += 1
            print(f' -> Step {steps} (states: {len(machines)})', end=' ' * 9 + '\r')
            machines = list(chain.from_iterable(machine.get_moves(skip_hashes) for machine in machines))
        return steps


def main():
    machines = list(map(Machine.from_manual_line, open('.input.txt').readlines()))

    total = 0
    for i, machine in enumerate(machines):
        print(f'{i + 1}/{len(machines)}:', machine.state, [" ".join(map(str, b)).join('()') for b in machine.buttons])
        solution = machine.solve()
        print('\nSolved:', solution, end='\n\n')
        total += solution

    print(total)


if __name__ == '__main__':
    main()

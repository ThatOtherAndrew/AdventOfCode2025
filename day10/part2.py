class Machine:
    def __init__(self, state: list[int], buttons: list[tuple[int, ...]], presses: int):
        self.state = state
        # prioritise buttons which can increment the most
        self.buttons = sorted(buttons, key=len, reverse=True)
        self.presses = presses
        self.is_invalid = min(state) < 0 or not self.buttons

    @staticmethod
    def from_manual_line(line: str) -> Machine:
        parts = line.split()
        state = list(map(int, parts[-1][1:-1].split(',')))
        buttons = [tuple(map(int, part[1:-1].split(','))) for part in parts[1:-1]]
        return Machine(state, buttons, 0)

    def press(self, button: tuple[int, ...], presses: int) -> Machine:
        new_state = self.state.copy()
        for i in button:
            new_state[i] -= presses

        # remove buttons which cause invalid states
        buttons = [b for b in self.buttons if all(self.state[i] > 0 for i in b)]

        return Machine(new_state, buttons, self.presses + presses)

    def max_presses(self, button: tuple[int, ...]) -> int:
        return min(self.state[i] for i in button)

    def solve(self) -> int | None:
        machine = self
        if machine.is_invalid:
            return None

        # max out all required presses
        changed = True
        while changed:
            changed = False
            for i in range(len(machine.state)):
                relevant_buttons = [b for b in machine.buttons if i in b]
                if len(relevant_buttons) == 1:  # no other button can increment index i, therefore this must be pressed
                    new_machine = machine.press(relevant_buttons[0], machine.state[i])
                    if not new_machine.is_invalid:
                        machine = new_machine
                        changed = True

        # guess and backtrack
        for presses in range(machine.max_presses(machine.buttons[0]), 0, -1):
            new_machine = Machine(machine.state.copy(), machine.buttons[1:], machine.presses)
            new_machine.press(machine.buttons[0], presses)
            solution = new_machine.solve()
            if solution is not None:
                return solution

        return None


def main():
    machines = list(map(Machine.from_manual_line, open('input.txt').readlines()))
    for machine in machines:
        print(machine.solve())


if __name__ == '__main__':
    main()

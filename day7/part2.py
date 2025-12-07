from collections import defaultdict

import numpy as np

def main():
    grid = np.array([list(line.strip()) for line in open('.input.txt')])
    # map beam positions (x/column value) to number of ways to get to that position
    beams: dict[int, int] = {np.where(grid == 'S')[1][0]: 1}

    for y in range(len(grid)):
        new_beams: dict[int, int] = defaultdict(int)

        for beam, count in beams.items():
            new_positions = (beam - 1, beam + 1) if grid[y, beam] == '^' else (beam,)
            for position in new_positions:
                new_beams[position] += count

        beams = new_beams

    print(sum(beams.values()))


if __name__ == '__main__':
    main()

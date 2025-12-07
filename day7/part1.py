import numpy as np

def main():
    grid = np.array([list(line.strip()) for line in open('input.txt')])
    beams = {np.where(grid == 'S')[1][0]}
    splits = 0

    for y in range(len(grid)):
        new_beams: set[int] = set()

        for beam in beams:
            if grid[y, beam] == '^':  # splitter beams
                new_beams.update((beam - 1, beam + 1))
                splits += 1
            else:  # just flowing downwards
                new_beams.add(beam)

        beams = new_beams

    print(splits)

if __name__ == '__main__':
    main()

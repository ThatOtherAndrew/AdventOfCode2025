import numpy as np

def main():
    grid = np.array([list(line.strip()) for line in open('input.txt')])
    grid = np.pad(grid, 1, constant_values='#') # pad array to avoid grid border edge cases
    removed = True
    total = 0

    while removed:
        removed = False
        for y in range(grid.shape[0] - 2):
            for x in range(grid.shape[1] - 2):
                subsection = grid[y:y + 3, x:x + 3] # iterate "sliding" 3x3 subgrid across all positions
                if subsection[1,1] != '@':
                    continue # skip if not centred on paper roll
                if np.sum(subsection == '@') <= 4: # <= 4 instead of < 4 to account for centre roll
                    subsection[1,1] = '.' # also mutates original array
                    total += 1
                    removed = True

    print(total)


if __name__ == '__main__':
    main()

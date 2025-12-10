import math
from itertools import combinations


def main():
    junction_boxes = [tuple(map(int, line.split(','))) for line in open('input.txt')]
    sorted_pairs = sorted(combinations(junction_boxes, 2), key=lambda x: math.dist(x[0], x[1]))

    circuits: list[set[tuple[int, ...]]] = []
    for pair in sorted_pairs:
        new_circuit = set(pair)
        new_circuits = [new_circuit]
        for circuit in circuits:
            if new_circuit.intersection(circuit):
                # if the two circuits overlap, merge them
                new_circuit.update(circuit)
            else:
                # otherwise keep the original circuit
                new_circuits.append(circuit)
        circuits = new_circuits

        # exit if all junction boxes are connected in one circuit
        if len(circuits[0]) == len(junction_boxes):
            print(pair[0][0] * pair[1][0])
            break


if __name__ == '__main__':
    main()

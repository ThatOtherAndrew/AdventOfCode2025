import networkx as nx


def main():
    graph = nx.DiGraph()
    for line in open('input.txt'):
        node, outputs = line.split(': ')
        graph.add_edges_from([(node, output) for output in outputs.split()])

    print(len(list(nx.all_simple_paths(graph, source='you', target='out'))))


if __name__ == '__main__':
    main()

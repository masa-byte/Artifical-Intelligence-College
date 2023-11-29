import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import node
import a_star


def visualize_graph(graph):
    G = nx.Graph()

    for i in range(n):
        for j in range(n):
            G.add_node(
                (i, j), color=graph[i][j].color, heuristics=graph[i][j].heuristics
            )

    for i in range(n):
        for j in range(n):
            for dest_node, weight in graph[i][j].edges:
                G.add_edge((i, j), (dest_node.i, dest_node.j), weight=weight)

    pos = {(i, j): (j, -i) for i in range(n) for j in range(n)}
    node_colors = [graph[i][j].color for i in range(n) for j in range(n)]
    node_labels = {(i, j): graph[i][j].heuristics for i in range(n) for j in range(n)}

    plt.title("Graph with Colored Nodes and Heuristics")
    nx.draw(
        G,
        pos,
        with_labels=False,
        font_weight="bold",
        node_size=700,
        node_color=node_colors,
        font_size=8,
        edge_color="gray",
    )
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_color="black")

    plt.show()


def calculate_heuristics(dest_i, dest_j, i, j):
    return abs(dest_i - i) + abs(dest_j - j)


if __name__ == "__main__":
    n = 4
    start_i = 0
    start_j = 0
    dest_i = 2
    dest_j = 1
    red_i = [1, 3]
    red_j = [1, 2]

    graph = np.array(
        [
            [
                node.Node("gray", calculate_heuristics(dest_i, dest_j, i, j), i, j)
                for j in range(n)
            ]
            for i in range(n)
        ]
    )

    # starting node
    graph[start_i][start_j].color = "blue"

    # red nodes
    for i, j in zip(red_i, red_j):
        graph[i][j].color = "red"
        graph[i][j].heuristics = float("inf")

    # green node
    graph[dest_i][dest_j].color = "green"
    graph[dest_i][dest_j].heuristics = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j].color == "red":
                continue
            if i < n - 1 and graph[i + 1][j].color != "red":
                graph[i][j].add_edge(graph[i + 1][j], 1)  # Edge down
            if i > 0 and graph[i - 1][j].color != "red":
                graph[i][j].add_edge(graph[i - 1][j], 1)  # Edge up
            if j < n - 1 and graph[i][j + 1].color != "red":
                graph[i][j].add_edge(graph[i][j + 1], 1)  # Edge right
            if j > 0 and graph[i][j - 1].color != "red":
                graph[i][j].add_edge(graph[i][j - 1], 1)  # Edge left

    visualize_graph(graph)

    path = a_star.a_star(graph, graph[start_i][start_j], graph[dest_i][dest_j])
    for path_node in path:
        print(path_node)

    graph2 = graph.copy()
    for path_node in path:
        graph2[path_node.i][path_node.j].color = "yellow"

    visualize_graph(graph2)

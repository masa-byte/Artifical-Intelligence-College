# Implementirati Backtracking traženje u kombinaciji sa Forward checking tehnikom i LCV
# heuristikom za bojenje čvorova grafa sa tri boje (crvena, zelena i plava) tako da ni jedna dva
# susedna čvora nemaju istu boju.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import node
import search


class Graph:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.graph = self.form_graph()

    def form_graph(self):
        graph = np.array([[node.Node(i, j) for j in range(self.j)] for i in range(self.i)])
        graph[0][0].add_edge(graph[1][0], 1)
        graph[1][0].add_edge(graph[0][0], 1)

        graph[1][0].add_edge(graph[2][0], 1)
        graph[2][0].add_edge(graph[1][0], 1)

        graph[2][0].add_edge(graph[3][0], 1)
        graph[3][0].add_edge(graph[2][0], 1)

        graph[3][0].add_edge(graph[4][0], 1)
        graph[4][0].add_edge(graph[3][0], 1)

        graph[0][0].add_edge(graph[4][0], 1)
        graph[4][0].add_edge(graph[0][0], 1)

        graph[1][0].add_edge(graph[4][0], 1)
        graph[4][0].add_edge(graph[1][0], 1)

        graph[1][0].add_edge(graph[3][0], 1)
        graph[3][0].add_edge(graph[1][0], 1)
        return graph

    def visualize_graph(self):
        G = nx.Graph()

        for i in range(self.i):
            for j in range(self.j):
                G.add_node((i, j), color=self.graph[i][j].color)

        for i in range(self.i):
            for j in range(self.j):
                for dest_node, weight in self.graph[i][j].edges:
                    G.add_edge((i, j), (dest_node.i, dest_node.j), weight=weight)

        pos = nx.circular_layout(G)
        node_colors = [
            self.graph[i][j].color
            for i in range(self.i)
            for j in range(self.j)
        ]

        plt.title("Graph with Colored Nodes")
        nx.draw(
            G,
            pos,
            font_weight="bold",
            node_size=700,
            node_color=node_colors,
            font_size=8,
            edge_color="gray",
        )
        nx.draw_networkx_labels(G, pos, font_size=8, font_color="black")

        plt.show()


if __name__ == "__main__":
    i = 5
    j = 1
    graph = Graph(i, j)
    search.depth_first_search(graph, graph.graph[0][0])

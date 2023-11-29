class Node:
    def __init__(self, color, heuristics, i , j):
        self.color = color
        self.heuristics = heuristics
        self.i = i
        self.j = j
        self.edges = []

    def add_edge(self, node, cost):
        self.edges.append((node, cost))

    def __str__(self):
        return f"Node({self.color}, {self.heuristics}, position: ({self.i}, {self.j}))"
    
    def print_edges(self):
        for edge in self.edges:
            print(f"Node({edge[0]}), weight {edge[1]})")
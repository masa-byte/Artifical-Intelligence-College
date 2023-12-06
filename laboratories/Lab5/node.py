class Node:
    def __init__(self, i, j):
        self.color = "gray"
        self.i = i
        self.j = j
        self.edges = []
        self.available_colors = ["blue", "green", "red"]

    def add_edge(self, node, cost):
        self.edges.append((node, cost))

    def remove_color(self, color):
        if color in self.available_colors:
            self.available_colors.remove(color)
    

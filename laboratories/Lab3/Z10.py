import queue
import networkx as nx
import matplotlib.pyplot as plt
import copy


def depth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False
    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        # process(node)
        for dest in reversed(graph[node]):
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                stack_nodes.put(dest)
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path


def remove_path_edges(graph, path):
    modified_graph = copy.deepcopy(graph)
    for i in range(len(path) - 1):
        start_node = path[i]
        end_node = path[i + 1]
        modified_graph[start_node].remove(end_node)
        modified_graph[end_node].remove(start_node)
    return modified_graph


def find_path_with_third_node(start_node, end_node, add_node, graph):
    modified_graph_path1 = copy.deepcopy(graph)
    while True:
        path1 = depth_first_search(modified_graph_path1, start_node, add_node)
        if len(path1) == 0:
            return []
        modified_graph_path1 = remove_path_edges(modified_graph_path1, path1)

        modified_graph_path2 = copy.deepcopy(graph)
        path2 = depth_first_search(modified_graph_path2, add_node, end_node)

        while True:
            if any(node in path2[1:] for node in path1):
                modified_graph_path2 = remove_path_edges(modified_graph_path2, path2)
                path2 = depth_first_search(modified_graph_path2, add_node, end_node)
                if len(path2) == 0:
                    break
            else:
                return path1 + path2[1:]


if __name__ == "__main__":
    graph_simple = {
        "A": ["B", "C", "J"],
        "B": ["A", "E"],
        "C": ["A", "G"],
        "D": ["H"],
        "E": ["G", "I", "B"],
        "F": ["J"],
        "G": ["C", "E"],
        "H": ["D"],
        "I": ["J", "E"],
        "J": ["A", "F", "I"],
    }

    G = nx.Graph(graph_simple)
    plt.subplot(121)
    pos = nx.circular_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_size=8,
        edge_color="gray",
    )

    path = find_path_with_third_node("A", "J", "G", graph_simple)
    P = nx.Graph()
    for i in range(len(path) - 1):
        start_node = path[i]
        end_node = path[i + 1]
        P.add_edge(start_node, end_node)
    plt.subplot(122)
    pos = nx.circular_layout(P)
    nx.draw(
        P,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_size=8,
        edge_color="gray",
    )

    plt.show()

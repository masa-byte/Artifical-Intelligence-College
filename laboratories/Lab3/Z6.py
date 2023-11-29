import networkx as nx
import matplotlib.pyplot as plt
import searches


def form_tree_dfs(start_node):
    tree = dict()
    _ = searches.depth_first_search(graph_simple, start_node, None, tree)
    return tree


def form_tree_bfs(start_node):
    tree = dict()
    _ = searches.breadth_first_search(graph_simple, start_node, None, tree)
    return tree


if __name__ == "__main__":
    graph_simple = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": ["G", "I", "A"],
        "F": ["J"],
        "G": ["J"],
        "H": [],
        "I": ["J"],
        "J": ["C"],
    }

    G = nx.DiGraph(graph_simple)

    pos = nx.circular_layout(G)
    plt.subplot(131)
    plt.title("Graph")
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

    tree_dfs = form_tree_dfs("F")
    T = nx.DiGraph(tree_dfs)
    pos = nx.circular_layout(T)
    plt.subplot(132)
    plt.title("DFS Tree")
    nx.draw(
        T,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="purple",
        font_size=8,
        edge_color="skyblue",
    )

    tree_bfs = form_tree_bfs("F")
    T = nx.DiGraph(tree_bfs)
    pos = nx.circular_layout(T)
    plt.subplot(133)
    plt.title("BFS Tree")
    nx.draw(
        T,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="purple",
        font_size=8,
        edge_color="skyblue",
    )
    plt.show()

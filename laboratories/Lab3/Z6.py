import queue
import networkx as nx
import matplotlib.pyplot as plt


def breadth_first_search(graph, start, end, tree):
    if start is end:
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found_dest = False
    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        if prev_nodes[node] is not None:
            tree[prev_nodes[node]].append(node)
        if node not in tree:
            tree[node] = []
        # process(node)
        for dest in reversed(graph[node]):
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                queue_nodes.put(dest)
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path


def depth_first_search(graph, start, end, tree):
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
        if prev_nodes[node] is not None:
            tree[prev_nodes[node]].append(node)
        if node not in tree:
            tree[node] = []
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


def form_tree_dfs(start_node):
    tree = dict()
    _ = depth_first_search(graph_simple, start_node, None, tree)
    return tree


def form_tree_bfs(start_node):
    tree = dict()
    _ = breadth_first_search(graph_simple, start_node, None, tree)
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

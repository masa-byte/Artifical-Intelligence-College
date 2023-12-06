import copy


def lcv_sort(node, colors, graph):
    return sorted(
        colors,
        key=lambda c: sum(
            1
            for neighbor, _ in node.edges
            if neighbor.color == "gray" and c in neighbor.available_colors
        ),
        reverse=True,
    )


def recursive_dfs(graph, node):
    successful = False
    node_colors_copy = lcv_sort(node, copy.deepcopy(node.available_colors), graph)

    while successful is False and node_colors_copy != []:
        dest_nodes_colors_copy = []
        node.color = node_colors_copy.pop()
        graph.visualize_graph()
        successful = True
        # forward checking
        index = 0
        for dest_node, weight in node.edges:
            if dest_node.color == "gray":
                dest_nodes_colors_copy.append(copy.deepcopy(dest_node.available_colors))
                dest_node.remove_color(node.color)
                if dest_node.available_colors == []:
                    dest_node.available_colors = dest_nodes_colors_copy[index]
                    successful = False
                    break
                index += 1

        index = 0
        if successful is True:
            for dest_node, weight in node.edges:
                if dest_node.color == "gray":
                    successful = recursive_dfs(graph, dest_node)
                    if successful is True:
                        break
                    else:
                        dest_node.color = "gray"
                        dest_node.available_colors = dest_nodes_colors_copy[index]
                        index += 1

    return successful


def depth_first_search(graph, start):
    successful = recursive_dfs(graph, start)

    for i in range(graph.i):
        for j in range(graph.j):
            if graph.graph[i][j].color == "gray":
                return recursive_dfs(graph, graph.graph[i][j])

    return successful

def a_star(graph, start, end):
    found_end = False
    open_set = set([start])
    closed_set = set()
    g = {}
    prev_nodes = {}
    g[start] = 0
    prev_nodes[start] = None

    while len(open_set) > 0 and (not found_end):
        node = None
        for next_node in open_set:
            if (
                node is None
                or g[next_node] + graph[next_node.i][next_node.j].heuristics
                < g[node] + graph[node.i][node.j].heuristics
            ):
                node = next_node
                if node == end:
                    found_end = True
                    break

        for m, cost in graph[node.i][node.j].edges:
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                prev_nodes[m] = node
                g[m] = g[node] + cost
            else:
                if g[m] > g[node] + cost:
                    g[m] = g[node] + cost
                    prev_nodes[m] = node

        open_set.remove(node)
        closed_set.add(node)

    path = []
    if found_end:
        prev = end
        while prev_nodes[prev] is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.append(start)
        path.reverse()

    return path

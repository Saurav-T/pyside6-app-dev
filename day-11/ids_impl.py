graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def dls(graph, node, goal, limit):
    if node == goal:
        return True

    if limit <= 0:
        return False

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit - 1):
            return True

    return False


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit = {depth}")

        if dls(graph, start, goal, depth):
            print(f"Goal found at depth {depth}")
            return True

    return False


ids(graph, 'A', 'G', 5)
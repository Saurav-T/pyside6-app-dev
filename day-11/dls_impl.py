graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
def dls(graph, node, goal, limit, depth=0):
    print(f"Visiting {node} at depth {depth}")

    if node == goal:
        return True

    if depth == limit:
        return False

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, limit, depth + 1):
            return True

    return False


# Search for G with depth limit 2
found = dls(graph, 'A', 'G', limit=2)

if found:
    print("Goal found!")
else:
    print("Goal not found within depth limit.")
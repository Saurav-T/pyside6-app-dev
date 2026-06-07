from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': [],
    'D': ['E', 'F'],
    'E': [],
    'F': []
}
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 6,
    'E': 2,
    'F': 6,
    'G': 0
}

def a_star(graph, start, goal, h):

    pq = []
    heapq.heappush(pq, (0 + h[start], 0, start))

    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        print(f"Visiting {node} with f={f}, g={g}")

        if node == goal:
            print("Goal reached!")
            return
        
        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor))

a_star(graph, 'A', 'G', h)
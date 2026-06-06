import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0
}

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        _, node = heapq.heappop(pq)

        print(node, end=" ")

        if node == goal:
            print("\nGoal reached!")
            return

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))


greedy_best_first_search(graph, 'A', 'G', heuristic)
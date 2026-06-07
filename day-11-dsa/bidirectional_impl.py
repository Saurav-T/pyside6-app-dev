from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['C', 'G'],
    'G': ['D', 'E']
}

start = 'A'
goal = 'G'

front = {start}
back = {goal}

while front and back:
    if front & back:
        print("Searches met at:", front & back)
        break

    new_front = set()
    for node in front:
        for neighbor in graph[node]:
            new_front.add(neighbor)

    front = new_front
print("Hello, World!")

from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Real-world communication system example
communication_network = {
    "Router": ["Switch1", "Switch2"],
    "Switch1": ["Router", "PC1", "PC2"],
    "Switch2": ["Router", "PC3", "PC4"],
    "PC1": ["Switch1"],
    "PC2": ["Switch1"],
    "PC3": ["Switch2"],
    "PC4": ["Switch2"],
}

print("DFS Traversal of Communication Network:")
dfs(communication_network, "Router")
print("\nBFS Traversal of Communication Network:")
bfs(communication_network, "Router")

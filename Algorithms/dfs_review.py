graph = {
    'G': ['D'],
    'D': ['G', 'C', 'E'],
    'C': ['D', 'B'],
    'E': ['D', 'F'],
    'B': ['C', 'A', 'H'],
    'F': ['E'],
    'A': ['B'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'M': ['H'],
    'K': ['J', 'L'],
    'L': ['K']
}

from collections import deque

def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited

print(' -> '.join(dfs(graph, 'G')))


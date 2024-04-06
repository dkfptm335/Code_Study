import sys
from collections import deque

sys.setrecursionlimit(10**6)

nodeCount, edgeCount, startNode = map(int, input().split())
graph = {i: [] for i in range(1, nodeCount + 1)}
for _ in range(edgeCount):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

def dfs(graph, start, visited = deque()):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            visited = dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    visited = deque()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += graph[node]
    return visited

print(' '.join(map(str, dfs(graph, startNode))))
print(' '.join(map(str, bfs(graph, startNode))))

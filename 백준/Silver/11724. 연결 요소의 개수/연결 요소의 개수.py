import sys
from collections import deque

node, edge = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, node + 1)}
visited = {i: False for i in range(1, node + 1)}
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


count = 0

for i in range(1, node + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)

import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(1, N + 1)}
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()


count = 0


def dfs(v):
    global count
    count += 1
    visited[v] = count
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


dfs(R)

for i in range(1, N + 1):
    print(visited[i])
    
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
    graph[key].sort(reverse=True)


queue = deque()
queue.append(R)
count = 1
visited[R] = count

while queue:
    node = queue.popleft()
    for next_node in graph[node]:
        if visited[next_node] == 0:
            count += 1
            visited[next_node] = count
            queue.append(next_node)

for i in range(1, N + 1):
    print(visited[i])

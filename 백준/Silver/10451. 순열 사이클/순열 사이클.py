import sys
from collections import deque


def bfs(graph, startNode, visit):
    queue = deque([startNode])
    visit[startNode] = True

    while queue:
        currenNode = queue.popleft()
        if not visit[graph[currenNode]]:
            visit[graph[currenNode]] = True
            queue.append(graph[currenNode])


t = int(sys.stdin.readline().strip())
for tc in range(1, t + 1):
    N = int(sys.stdin.readline().strip())
    permutation = list(map(int, sys.stdin.readline().strip().split()))
    cycle = {i + 1: permutation[i] for i in range(len(permutation))}
    visited = {k: False for k in cycle.keys()}
    count = 0

    for num in cycle.keys():
        if not visited[num]:
            bfs(cycle, num, visited)
            count += 1

    print(count)

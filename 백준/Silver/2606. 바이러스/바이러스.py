from collections import deque
import sys


def bfs(start):
    queue = deque([start])

    while queue:
        currentNode = queue.popleft()
        if currentNode not in infected:
            infected.append(currentNode)
            queue += graph[currentNode]


nodeCount = int(sys.stdin.readline())
edgeCount = int(sys.stdin.readline())
graph = {i: [] for i in range(1, nodeCount + 1)}
for i in range(1, edgeCount + 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


for key in graph:
    graph[key].sort()

infected = list()
bfs(1)

print(len(infected) - 1)

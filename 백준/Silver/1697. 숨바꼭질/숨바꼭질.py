import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
time = 0
visited = [0] * 100001
queue = deque([N])

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == K:
            print(time)
            sys.exit()
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = 1
                queue.append(nx)
    time += 1
    
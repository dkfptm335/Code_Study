import sys
from collections import deque

dx = [1, 0]
dy = [0, 1]
queue = deque([(0, 0)])

n, m = map(int, sys.stdin.readline().strip().split())
maps = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

print("Yes" if visited[m - 1][n - 1] else "No")

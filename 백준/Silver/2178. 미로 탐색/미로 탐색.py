import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]
queue = deque([(0, 0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] += visited[x][y] + 1

print(visited[-1][-1])

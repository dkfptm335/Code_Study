import sys
from collections import deque


M, N = map(int, sys.stdin.readline().strip().split())
field = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if field[nx][ny] == 0:
                field[nx][ny] = field[x][y] + 1
                queue.append((nx, ny))

day = 0

for row in field:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)

    day = max(day, max(row))

print(day - 1)

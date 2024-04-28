import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split())
field = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if field[i][j][k] == 1:
                queue.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for s in range(6):
            nz, nx, ny = z + dz[s], x + dx[s], y + dy[s]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if field[nz][nx][ny] == 0:
                    field[nz][nx][ny] = field[z][x][y] + 1
                    queue.append((nz, nx, ny))


bfs()
cannotComplete = False
day = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if field[i][j][k] == 0:
                cannotComplete = True
            day = max(day, field[i][j][k])

print(-1 if cannotComplete else day - 1)

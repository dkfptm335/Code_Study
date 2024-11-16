import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

# 탐색 시작 지점 큐에 추가
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))


while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = box[x][y] + 1

day = 0

# 모든 토마토가 익었는지 확인
for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)

    day = max(day, max(row))

print(day - 1)

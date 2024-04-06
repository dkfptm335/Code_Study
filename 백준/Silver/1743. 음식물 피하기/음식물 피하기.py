from sys import stdin
from collections import deque


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    trashSize = 0

    while queue:
        cx, cy = queue.popleft()
        visited[cx][cy] = True
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and pathWay[cx][cy] == pathWay[nx][ny]:
                    trashSize += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return trashSize + 1


N, M, K = map(int, stdin.readline().strip().split())
batch = []
for _ in range(K):
    x, y = map(int, stdin.readline().strip().split())
    batch.append((x - 1, y - 1))

pathWay = [['.'] * M for _ in range(N)]
for x, y in batch:
    pathWay[x][y] = '#'

trash = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and pathWay[i][j] == '#':
            trash.append(bfs(i, j))

print(max(trash))

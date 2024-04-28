import sys
from collections import deque


def bfs(start_x, start_y, rain):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    safeRegions = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and region[nx][ny] > rain:
                    safeRegions += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return safeRegions


N = int(sys.stdin.readline().strip())
region = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
maxHeight = 0
for row in region:
    maxHeight = max(maxHeight, max(row))

maxRegions = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for rainHeight in range(maxHeight):
    visited = [[False] * N for _ in range(N)]
    tmpRegions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and region[i][j] > rainHeight:
                tmpRegions.append(bfs(i, j, rainHeight))

    maxRegions = max(maxRegions, len(tmpRegions))

print(maxRegions)

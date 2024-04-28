import sys
from collections import deque


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    landSize = 1

    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    landSize += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return landSize


while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    lands = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == 1:
                lands.append(bfs(i, j))

    print(len(lands))

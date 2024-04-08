import sys
from collections import deque


def bfs(graph, start_x, start_y, visit):
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cabbage = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and graph[x][y] == graph[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    cabbage += 1

    return cabbage


t = int(sys.stdin.readline())

for tc in range(1, t + 1):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        row, col = map(int, sys.stdin.readline().strip().split())
        field[col][row] = 1

    cabbages = []

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                cabbages.append(bfs(field, i, j, visited))

    print(len(cabbages))

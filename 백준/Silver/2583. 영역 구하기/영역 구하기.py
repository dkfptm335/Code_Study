import sys
from collections import deque


def bfs(graph, start_x, start_y, visit):
    areaSize = 1
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    areaSize += 1

    return areaSize


M, N, K = map(int, sys.stdin.readline().strip().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    rux, ruy, ldx, ldy = map(int, sys.stdin.readline().strip().split())
    for i in range(rux, ldx):
        for j in range(ruy, ldy):
            board[i][j] = 1

visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
areas = []

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 0:
            areas.append(bfs(board, i, j, visited))

areas.sort()
print(len(areas))
print(' '.join(list(map(str, areas))))

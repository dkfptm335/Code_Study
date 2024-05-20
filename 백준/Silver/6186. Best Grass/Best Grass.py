import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, start_x, start_y, visit):
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True

    sharp = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[x][y] == graph[nx][ny] and not visit[nx][ny]:
                    sharp += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))

    return sharp


n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
sharps = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == "#":
            sharps.append(bfs(board, i, j, visited))

print(len(sharps))

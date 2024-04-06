from collections import deque
from sys import stdin


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


n, m = map(int, stdin.readline().strip().split())
maze = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if maze[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()

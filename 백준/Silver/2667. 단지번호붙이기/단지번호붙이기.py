from collections import deque
import sys

n = int(sys.stdin.readline())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    apartment = 1
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == board[x][y] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    apartment += 1

    return apartment


apartments = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            apartments.append(bfs(i, j))

apartments.sort()
print(len(apartments))
for apart in apartments:
    print(apart)
    
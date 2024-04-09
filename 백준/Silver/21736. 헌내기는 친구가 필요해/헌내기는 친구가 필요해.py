import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
campus = [list(sys.stdin.readline().strip()) for _ in range(N)]


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    people = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                elif campus[nx][ny] == 'P' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    people += 1

    return people


for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            answer = bfs(i, j)
            print(answer if answer else 'TT')
            
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visit, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True
    picture = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[x][y] == graph[nx][ny] and not visit[nx][ny]:
                    picture += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))

    return picture


n, m = map(int, sys.stdin.readline().strip().split())
frame = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
pictures = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and frame[i][j] == 1:
            pictures.append(bfs(frame, visited, i, j))

print(len(pictures))
if pictures:
    print(max(pictures))
else:
    print(0)

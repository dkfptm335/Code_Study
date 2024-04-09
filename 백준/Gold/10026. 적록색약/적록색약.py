import sys
from collections import deque

N = int(sys.stdin.readline())
picture = [list(sys.stdin.readline().strip()) for _ in range(N)]
specialPic = [list(''.join(row).replace('G', 'R')) for row in picture]
visited = [[False] * len(picture[0]) for _ in range(N)]
specialVisited = [[False] * len(picture[0]) for _ in range(N)]


def bfs(graph, start_x, start_y, visit):
    size = 1
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == graph[x][y] and not visit[nx][ny]:
                    size += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))

    return size


normal = []
special = []

for i in range(N):
    for j in range(len(picture[0])):
        if picture[i][j] == 'R' and not visited[i][j]:
            normal.append(bfs(picture, i, j, visited))
        if specialPic[i][j] == 'R' and not specialVisited[i][j]:
            special.append(bfs(specialPic, i, j, specialVisited))
        if picture[i][j] == 'B' and not visited[i][j]:
            normal.append(bfs(picture, i, j, visited))
        if specialPic[i][j] == 'B' and not specialVisited[i][j]:
            special.append(bfs(specialPic, i, j, specialVisited))
        if picture[i][j] == 'G' and not visited[i][j]:
            normal.append(bfs(picture, i, j, visited))

print(len(normal), len(special))

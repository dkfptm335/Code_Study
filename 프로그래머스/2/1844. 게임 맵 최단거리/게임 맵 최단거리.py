from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visit, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visit[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))


def solution(maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    bfs(maps, visited, 0, 0)
    return -1 if visited[len(maps) - 1][len(maps[0]) - 1] == 0 else visited[len(maps) - 1][len(maps[0]) - 1]
    
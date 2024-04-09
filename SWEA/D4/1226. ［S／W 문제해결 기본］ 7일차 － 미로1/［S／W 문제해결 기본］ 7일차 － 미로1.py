from collections import deque

for tc in range(1, 11):
    testNum = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    isPossible = False
    visited = [[False] * 16 for _ in range(16)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                queue.append((i, j))
                break

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                if maze[nx][ny] == 3 and not visited[nx][ny]:
                    isPossible = True
                    break

    print(f"#{tc} {1 if isPossible else 0}")
    
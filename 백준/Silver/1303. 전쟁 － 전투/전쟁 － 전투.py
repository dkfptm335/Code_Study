import sys
from collections import deque


def bfs(MAP, start_x, start_y, visit):
    # 큐 생성
    queue = deque()
    # 상 하 좌 우 방향 벡터 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 탐색 시작 지점 큐에 추가
    queue.append((start_x, start_y))
    # 탐색 시작 지점 방문 처리
    visit[start_x][start_y] = True

    # 탐색 시작 지점과 인접한 같은 병사의 수
    soldier = 0

    # 큐가 빌 때까지 계속
    while queue:
        # 현재 탐색 지점 pop
        x, y = queue.popleft()
        for i in range(4):
            # 새로운 좌표 지정
            nx, ny = x + dx[i], y + dy[i]
            # 조건 설정
            if 0 <= nx < m and 0 <= ny < n and MAP[x][y] == MAP[nx][ny] and visit[nx][ny] == False:
                # 새로운 좌표 방문 처리
                visit[nx][ny] = True
                # 새로운 좌표 큐에 추가
                queue.append((nx, ny))
                # 병사 1명 추가
                soldier += 1

    # 탐색 시작 지점의 병사 1명 추가한 후 리턴
    return soldier + 1


n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
wSum = 0
bSum = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            soldiers = bfs(board, i, j, visited)

            if board[i][j] == 'W':
                wSum += soldiers ** 2
            else:
                bSum += soldiers ** 2

print(f"{wSum} {bSum}")

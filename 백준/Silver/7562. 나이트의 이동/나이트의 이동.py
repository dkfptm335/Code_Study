import sys
from collections import deque


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    chessBoard[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < I and 0 <= ny < I:
                if chessBoard[nx][ny] == 0:
                    chessBoard[nx][ny] = chessBoard[x][y] + 1
                    queue.append((nx, ny))


t = int(sys.stdin.readline().strip())
answers = []
for tc in range(1, t + 1):
    I = int(sys.stdin.readline().strip())
    chessBoard = [[0] * I for _ in range(I)]
    knightX, knightY = map(int, sys.stdin.readline().strip().split())
    targetX, targetY = map(int, sys.stdin.readline().strip().split())

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    bfs(knightX, knightY)
    answers.append(chessBoard[targetX][targetY] - 1)

for answer in answers:
    print(answer)

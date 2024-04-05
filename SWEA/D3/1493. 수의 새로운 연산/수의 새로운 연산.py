T = int(input())

board = [[0] * 1000 for _ in range(1000)]
board[0][0] = 1
x, y = 0, 1
for i in range(2, 50001, 1):
    board[x][y] = i
    if y - 1 >= 0:
        x += 1
        y -= 1
    else:
        x = 0
        y = len(board[0]) - board[0].count(0)


def find_position(n):
    global board
    for row in range(300):
        for col in range(300):
            if board[row][col] == n:
                return row, col


for tc in range(1, T + 1):
    p, q = map(int, input().split())
    px, py = find_position(p)
    qx, qy = find_position(q)

    print(f"#{tc} {board[px + qx + 1][py + qy + 1]}")

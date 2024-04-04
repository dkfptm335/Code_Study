def find_lu(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                return i, j


def find_rd(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[i]) - 1, -1, -1):
            if board[i][j] == '#':
                return i, j


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    isSquare = True

    # 좌상단 찾기
    lux, luy = find_lu(grid)
    rdx, rdy = find_rd(grid)

    for i in range(lux, rdx + 1):
        for j in range(luy, rdy + 1):
            if grid[i][j] == '.':
                isSquare = False
                break

    if rdx - lux != rdy - luy:
        isSquare = False

    print(f"#{tc} {'yes' if isSquare else 'no'}")

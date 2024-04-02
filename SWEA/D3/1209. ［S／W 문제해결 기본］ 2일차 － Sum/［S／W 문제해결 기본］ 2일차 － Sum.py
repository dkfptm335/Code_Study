for tc in range(1, 11):
    testNum = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    board_transpose = list(zip(*board))

    row_sum = []

    for row in board:
        row_sum.append(sum(row))

    for row in board_transpose:
        row_sum.append(sum(row))

    tmp = 0
    for i in range(len(board)):
        tmp += board[i][i]
    row_sum.append(tmp)

    tmp = 0
    for i in range(len(board)):
        tmp += board[i][-i - 1]
    row_sum.append(tmp)

    print(f"#{tc} {max(row_sum)}")

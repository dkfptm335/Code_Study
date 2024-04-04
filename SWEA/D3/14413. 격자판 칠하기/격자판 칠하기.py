t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    indexSum = {
        'sharpEven': 0,
        'sharpOdd' : 0,
        'dotEven': 0,
        'dotOdd': 0
    }

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                if (i + j) % 2 == 0:
                    indexSum['sharpEven'] += 1
                else:
                    indexSum['sharpOdd'] += 1
            elif board[i][j] == '.':
                if (i + j) % 2 == 0:
                    indexSum['dotEven'] += 1
                else:
                    indexSum['dotOdd'] += 1

    if (indexSum['sharpEven'] and indexSum['sharpOdd']) or (indexSum['dotEven'] and indexSum['dotOdd']) or \
            (indexSum['sharpEven'] and indexSum['dotEven']) or (indexSum['sharpOdd'] and indexSum['dotOdd']):
        print(f"#{tc} impossible")
    else:
        print(f"#{tc} possible")
        
def find_rd(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[i]) - 1, -1, -1):
            if board[i][j] == 1:
                return i, j


key = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    x, y = find_rd(arr)

    crypt = arr[x][y - 55:y + 1]
    parsedCrypt = []
    for i in range(0, 56, 7):
        parsedCrypt.append(''.join(map(str, crypt[i:i + 7])))

    plainTexts = [key[i] for i in parsedCrypt]
    sumOdd = 0
    sumEven = 0

    for i in range(len(plainTexts)):
        if i % 2 == 0:
            sumOdd += plainTexts[i]
        else:
            sumEven += plainTexts[i]

    if not (sumOdd * 3 + sumEven) % 10:
        print(f"#{tc} {sum(plainTexts)}")
    else:
        print(f"#{tc} 0")
        
import sys

board = [list(sys.stdin.readline().strip()) for _ in range(5)]
maxRowLength = 0
for row in board:
    maxRowLength = max(maxRowLength, len(row))

for i in range(5):
    if len(board[i]) < maxRowLength:
        for _ in range(maxRowLength - len(board[i])):
            board[i].append('*')

result = ''
for i in range(maxRowLength):
    for j in range(5):
        if board[j][i] != '*':
            result += board[j][i]

print(result)

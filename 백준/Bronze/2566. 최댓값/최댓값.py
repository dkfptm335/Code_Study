import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
maxVal = 0
maxI = 0
maxJ = 0

for i in range(9):
    for j in range(9):
        if maxVal < board[i][j]:
            maxVal = board[i][j]
            maxI = i
            maxJ = j

print(maxVal)
print(maxI + 1, maxJ + 1)

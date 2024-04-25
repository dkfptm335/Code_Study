import sys

maxIndex = 0
rectangles = []
for _ in range(4):
    lux, luy, rdx, rdy = map(int, sys.stdin.readline().split())
    maxIndex = max(maxIndex, max(lux, rdx, luy, rdy))
    rectangles.append((lux, luy, rdx, rdy))

board = [[0] * (maxIndex + 1) for _ in range(maxIndex + 1)]
for lux, luy, rdx, rdy in rectangles:
    for i in range(lux, rdx):
        for j in range(luy, rdy):
            board[i][j] = 1

answer = 0
for i in range(maxIndex + 1):
    for j in range(maxIndex + 1):
        if board[i][j] == 1:
            answer += 1

print(answer)

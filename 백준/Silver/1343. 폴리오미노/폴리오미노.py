import sys

board = sys.stdin.readline().strip()
while "XXXX" in board:
    board = board.replace("XXXX", "AAAA")

while "XX" in board:
    board = board.replace("XX", "BB")

print(-1 if "X" in board else board)

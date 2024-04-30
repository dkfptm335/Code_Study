import sys

N = int(sys.stdin.readline().strip())
board = [-1] * N
count = 0


def isPromising(depth):
    for i in range(depth):
        if board[i] == board[depth] or abs(board[i] - board[depth]) == abs(i - depth):
            return False
    return True


def backtracking(depth):
    global count
    if depth == N:
        count += 1
        return

    for i in range(N):
        board[depth] = i
        if isPromising(depth):
            backtracking(depth + 1)


backtracking(0)
print(count)

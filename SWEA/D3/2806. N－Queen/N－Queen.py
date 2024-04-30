t = int(input().strip())


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


answers = []
for tc in range(1, t + 1):
    N = int(input().strip())
    board = [-1] * N
    count = 0

    backtracking(0)
    answers.append(count)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")

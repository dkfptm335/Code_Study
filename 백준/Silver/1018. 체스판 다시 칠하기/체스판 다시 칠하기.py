def get_diff(A, B):
    count = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != B[i][j]:
                count += 1

    return count


N, M = map(int, input().split())

# N by M 행렬
board = [list(input()) for _ in range(N)]

# 8 by 8 행렬
chess_wb = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chess_bw = [row[::-1] for row in chess_wb]

min_diff = 64
for i in range(N - 7):
    for j in range(M - 7):
        A = [row[j:j + 8] for row in board[i:i + 8]]
        min_diff = min(min_diff, get_diff(A, chess_wb), get_diff(A, chess_bw))

print(min_diff)
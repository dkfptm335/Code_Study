N, M = map(int, input().split())

A, B = [], []

for i in range(N):
    tmp = [int(x) for x in input().split()]
    A.append(tmp)

for i in range(N):
    tmp = [int(x) for x in input().split()]
    B.append(tmp)

C = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for i in range(N):
    print(' '.join(map(str, C[i])))
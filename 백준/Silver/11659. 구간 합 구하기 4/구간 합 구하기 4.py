import sys

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
accum = 0
for i in range(N):
    accum += A[i]
    A[i] = accum
for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(A[b-1] - A[a-2] if a > 1 else A[b-1])
    
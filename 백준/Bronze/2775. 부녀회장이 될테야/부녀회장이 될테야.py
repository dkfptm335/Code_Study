import sys


T = int(sys.stdin.readline())
test_cases = {}

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apart = [[0 for _ in range(n)] for _ in range(k+1)]

    # 0층
    for j in range(n):
        apart[0][j] = j+1

    # 1층 이상
    for j in range(1, k+1):
        for l in range(n):
            for m in range(l+1):
                apart[j][l] += apart[j-1][m]

    test_cases[i] = apart[k][n-1]

for i in range(T):
    print(test_cases[i])
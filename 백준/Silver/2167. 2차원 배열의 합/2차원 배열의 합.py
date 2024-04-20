import sys

n, m = map(int, sys.stdin.readline().strip().split())
numbers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
k = int(sys.stdin.readline().strip())
queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
for query in queries:
    sumNum = 0
    i, j, x, y = query
    for k in range(i - 1, x):
        for l in range(j - 1, y):
            sumNum += numbers[k][l]

    print(sumNum)

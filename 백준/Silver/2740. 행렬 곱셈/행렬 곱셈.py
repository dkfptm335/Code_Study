import sys

n, m = map(int, sys.stdin.readline().strip().split())
aList = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().strip().split())
bList = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
result = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            result[x][y] += aList[x][z] * bList[z][y]

for row in result:
    print(' '.join(map(str, row)))

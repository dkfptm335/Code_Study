import sys

chess = list(map(int, sys.stdin.readline().split()))
original = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(original[i] - chess[i], end=' ')
    
import sys

N, M = map(int, sys.stdin.readline().strip().split())
setS = set([sys.stdin.readline().strip() for _ in range(N)])
inspectionSet = [sys.stdin.readline().strip() for _ in range(M)]
count = 0
for s in inspectionSet:
    if s in setS:
        count += 1

print(count)

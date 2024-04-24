import sys

a, b = map(int, sys.stdin.readline().strip().split())
aSet = set(list(map(int, sys.stdin.readline().strip().split())))
bSet = set(list(map(int, sys.stdin.readline().strip().split())))

# 대칭 차집합
print(len(aSet.difference(bSet)) + len(bSet.difference(aSet)))

import sys

n, m = map(int, sys.stdin.readline().strip().split())
nList = list(map(int, sys.stdin.readline().strip().split()))
mList = list(map(int, sys.stdin.readline().strip().split()))
resultList = nList + mList
resultList.sort()
print(' '.join(list(map(str, resultList))))

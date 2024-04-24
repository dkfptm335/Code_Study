import sys
from collections import deque

n = int(sys.stdin.readline().strip())
aList = list(map(int, sys.stdin.readline().strip().split()))
bList = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
aList.sort()
bList.sort(reverse=True)
for i in range(n):
    sum += aList[i] * bList[i]

print(sum)

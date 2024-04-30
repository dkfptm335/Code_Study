import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
visitLog = []


def dfs():
    if len(visitLog) == M:
        print(' '.join(map(str, visitLog)))
        return

    for i in range(1, N + 1):
        visitLog.append(i)
        dfs()
        visitLog.pop()


dfs()

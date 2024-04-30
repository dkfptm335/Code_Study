import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
visitLog = []


def dfs():
    if len(visitLog) == M:
        if visitLog == list(sorted(visitLog)):
            print(' '.join(map(str, visitLog)))
            return
        else:
            return

    for i in range(1, N + 1):
        if i not in visitLog:
            visitLog.append(i)
            dfs()
            visitLog.pop()


dfs()

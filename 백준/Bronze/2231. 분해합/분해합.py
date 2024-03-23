import sys


def degrade_sum(n):
    return n + sum(list(map(int, str(n))))


N = int(sys.stdin.readline())
for i in range(1, N + 1):
    if degrade_sum(i) == N:
        print(i)
        break
else:
    print(0)
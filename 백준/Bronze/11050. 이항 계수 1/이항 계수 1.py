import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


N, K = map(int, sys.stdin.readline().split())
print(combinations(N, K))

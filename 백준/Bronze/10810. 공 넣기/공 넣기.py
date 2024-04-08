import sys

N, M = map(int, sys.stdin.readline().split())
basket = {i: 0 for i in range(1, N + 1)}
queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
for query in queries:
    i, j, k = query
    for n in range(i, j + 1):
        basket[n] = k

print(' '.join(map(str, list(basket.values()))))

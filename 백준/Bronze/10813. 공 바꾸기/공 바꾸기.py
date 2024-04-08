import sys

N, M = map(int, sys.stdin.readline().split())
basket = {i: i for i in range(1, N + 1)}
queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
for query in queries:
    i, j = query
    basket[i], basket[j] = basket[j], basket[i]

print(' '.join(map(str, list(basket.values()))))

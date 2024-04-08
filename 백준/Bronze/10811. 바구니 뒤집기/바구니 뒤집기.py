import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1, N + 1)]
queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
for query in queries:
    i, j = query
    i -= 1
    j -= 1

    basket = basket[:i] + basket[i: j + 1][::-1] + basket[j + 1:]

print(' '.join(list(map(str, basket))))

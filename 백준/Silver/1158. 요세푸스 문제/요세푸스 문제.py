import sys
from collections import deque

N, K = map(int, input().split())
permutation = deque([i for i in range(1, N+1)])
log = []

count = 1

while permutation:
    if count == K:
        log.append(permutation.popleft())
        count = 1
    else:
        permutation.append(permutation.popleft())
        count += 1

print('<', end='')
print(', '.join(map(str, log)), end='')
print('>', end='')
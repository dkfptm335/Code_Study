import sys
from collections import deque

n = int(sys.stdin.readline().strip())
deq = deque([i for i in range(1, n + 1)])
while len(deq) != 1:
    print(deq.popleft(), end=' ')
    deq.append(deq.popleft())
print(deq[0])

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
queue = deque([i for i in range(1, N + 1)])
targets = list(map(int, sys.stdin.readline().strip().split()))
count = 0

for target in targets:
    if target == queue[0]:
        queue.popleft()
    elif queue.index(target) > len(queue) // 2:
        while not queue[0] == target:
            queue.appendleft(queue.pop())
            count += 1
        queue.popleft()
    else:
        while not queue[0] == target:
            queue.append(queue.popleft())
            count += 1
        queue.popleft()

print(count)

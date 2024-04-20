import sys
from collections import deque

x = int(sys.stdin.readline().strip())
rod = deque([64])

while x < sum(rod):
    tmp = rod.popleft()
    tmp /= 2
    if tmp + sum(rod) >= x:
        rod.appendleft(tmp)
    else:
        rod.appendleft(tmp)
        rod.appendleft(tmp)

print(len(rod))

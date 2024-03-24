import sys
from collections import deque

queue = deque()

N = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().strip().split() for _ in range(N)]

for command in commands:
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
stack = deque()
for _ in range(n):
    command = list(map(int, sys.stdin.readline().strip().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        print(stack.pop() if stack else -1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        print(1 if not stack else 0)
    else:
        print(stack[-1] if stack else -1)
        
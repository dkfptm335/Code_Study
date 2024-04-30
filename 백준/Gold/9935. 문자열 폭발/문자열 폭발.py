import sys
from collections import deque

s = deque(list(sys.stdin.readline().strip()))
explosion = list(sys.stdin.readline().strip())
stack = []

while s:
    if len(stack) < len(explosion):
        stack.append(s.popleft())
    elif len(stack) == len(explosion):
        if stack == explosion:
            stack.clear()
        else:
            stack.append(s.popleft())
    else:
        if stack[-len(explosion):] == explosion:
            del stack[-len(explosion):]
        else:
            stack.append(s.popleft())


if stack[-len(explosion):] == explosion:
    del stack[-len(explosion):]

print("FRULA" if not stack else ''.join(stack))

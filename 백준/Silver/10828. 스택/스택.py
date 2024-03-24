import sys

stack = []

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for _ in range(N)]

for command in commands:
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)
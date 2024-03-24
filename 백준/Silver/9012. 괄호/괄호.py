import sys


def check_vps(s):
    stack = []

    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)

    return not stack


T = int(sys.stdin.readline())
test_cases = {}

for i in range(1, T+1):
    test_cases[i] = 'YES' if check_vps(sys.stdin.readline().strip()) else 'NO'

for i in range(1, T+1):
    print(test_cases[i])

from collections import deque

t = int(input())

for tc in range(1, t + 1):
    s = deque(sorted(list(input().strip())))
    stack = list()

    while s:
        if not stack:
            stack.append(s.popleft())
        else:
            if stack[-1] == s[0]:
                stack.pop()
                s.popleft()
            else:
                stack.append(s.popleft())

    if not stack:
        print(f"#{tc} Good")
    else:
        print(f"#{tc} {''.join(stack)}")
        
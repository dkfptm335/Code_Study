from collections import deque

for tc in range(1, 11):
    testCase = list(input().split())
    passwordLength = int(testCase[0])
    password = deque(list(testCase[1]))
    stack = []

    while True:
        if len(password) == 0:
            break

        if len(stack) == 0:
            stack.append(password.popleft())

        else:
            if stack[-1] == password[0]:
                stack.pop()
                password.popleft()

            else:
                stack.append(password.popleft())

    print(f"#{tc} {''.join(stack)}")
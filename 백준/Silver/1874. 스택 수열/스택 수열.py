n = int(input())
stack = []
stack_log = []
current_num = 1

for i in range(n):
    num = int(input())
    while current_num <= num:
        stack.append(current_num)
        stack_log.append('+')
        current_num += 1
    if stack[-1] == num:
        stack.pop()
        stack_log.append('-')
    else:
        print('NO')
        exit(0)

for log in stack_log:
    print(log)
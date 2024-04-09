import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for tc in range(1, T + 1):
    commands = list(sys.stdin.readline().strip().replace('RR', ''))
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()
    if n == 0:
        newArr = deque()
    else:
        newArr = deque(list(map(int, arr[1:-1].split(','))))
    isErrored = False

    Rcount = 0
    
    for command in commands:
        if command == 'R':
            Rcount += 1
        else:
            if len(newArr) == 0:
                isErrored = True
                break
            if Rcount % 2 == 0:
                newArr.popleft()
            else:
                newArr.pop()
                
    if isErrored:
        print('error')
    else:
        if Rcount % 2 == 1:
            newArr.reverse()
        print('[' + ','.join(map(str, newArr)) + ']')
        
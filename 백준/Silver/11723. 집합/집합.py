import sys


def myAdd(x, arr):
    arr[int(x) - 1] = 1


def myRemove(x, arr):
    arr[int(x) - 1] = 0


def myCheck(x, arr):
    if arr[int(x) - 1] == 1:
        print(1)
    else:
        print(0)


def myToggle(x, arr):
    if arr[int(x) - 1] == 1:
        arr[int(x) - 1] = 0
    else:
        arr[int(x) - 1] = 1


def myAll():
    return [1] * 20


def myEmpty():
    return [0] * 20


M = int(sys.stdin.readline())
numbers = [0] * 20

for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        myAdd(command[1], numbers)
        
    elif command[0] == 'remove':
        myRemove(command[1], numbers)
        
    elif command[0] == 'check':
        myCheck(command[1], numbers)
        
    elif command[0] == 'toggle':
        myToggle(command[1], numbers)
        
    elif command[0] == 'all':
        numbers = myAll()
        
    elif command[0] == 'empty':
        numbers = myEmpty()
        
    else:
        print("Invalid command")

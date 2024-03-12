def push(str):
    str = str[len(str) - 1] + str[:len(str) - 1]
    return str

def solution(A, B):
    count = 0
    
    for i in range(len(A)):
        if A == B:
            return count
        else:
            A = push(A)
            count += 1
    
    if A == B:
        return count
    else:
        return -1
    
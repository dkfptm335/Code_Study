from collections import deque

def solution(A,B):
    A.sort()
    B.sort()
    A = deque(A)
    sum = 0
    
    for _ in range(len(A)):
        sum += A.popleft() * B.pop()
        
    return sum
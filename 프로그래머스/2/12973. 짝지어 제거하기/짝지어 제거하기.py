from collections import deque

def solution(s):
    # 정규표현식 쓰면 시간초과..
    
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return 1 if len(stack) == 0 else 0
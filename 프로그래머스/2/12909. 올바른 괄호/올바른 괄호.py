from collections import deque

def solution(s):
    # 괄호 개수 확인
    if s.count(r'(') != s.count(r')'):
        return False
    
    s = deque(s)
    stack = []
    
    while (len(s) != 0):
        if len(stack) == 0:
            stack.append(s.popleft())
            
        else:
            stack.append(s.popleft())
            if stack[-2] == r'(' and stack[-1] == r')':
                stack.pop()
                stack.pop()
                
    return True if len(stack) == 0 else False
from collections import deque

def isValid(s_orig):
    s = s_orig.copy()
    stack = []
    
    while len(s) != 0:
        if len(stack) == 0:
            stack.append(s.popleft())
            
        else:
            if (stack[-1] == '[' and s[0] == ']') or (stack[-1] == '(' and s[0] == ')') or (stack[-1] == '{' and s[0] == '}'):
                stack.pop()
                s.popleft()
            else:
                stack.append(s.popleft())
                
    if len(stack) == 0:
        return True
    else:
        return False
                
def solution(s):
    s = deque(s)
    count = 0
    
    for _ in range(len(s)):
        if isValid(s):
            count += 1
            
        s.append(s.popleft())
        
    return count
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def solution(n):
    i = 1
    
    while factorial(i) <= n:
        i += 1
        
    return i - 1

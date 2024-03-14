def solution(n):
    # Fibonacci: f(n+2) = f(n) + f(n+1), f(0) = 0, f(1) = 1
    values = [0, 1]
    
    for _ in range(n-1):
        values.append(values[-1]+values[-2])
        
    return values[n]%1234567
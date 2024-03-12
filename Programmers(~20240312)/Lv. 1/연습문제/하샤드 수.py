def solution(n):
    if n % sum([int(i) for i in str(n)]) == 0:
        return True
    else:
        return False

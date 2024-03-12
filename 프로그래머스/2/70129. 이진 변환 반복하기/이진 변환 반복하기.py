def solution(s):
    del_zero = 0
    loop = 0
    # 0제거
    while s != '1':
        loop += 1
        while '0' in s:
            del_zero += s.count('0')
            s = s.replace('0', '')

        s = bin(len(s))[2:]
    
    return [loop, del_zero]
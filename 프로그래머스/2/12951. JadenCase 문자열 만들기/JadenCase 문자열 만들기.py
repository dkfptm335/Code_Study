def solution(s):
    # 문자열 split
    s = s.split(' ')
    
    while ' ' in s:
        s.remove(' ')
    
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        
    return ' '.join(s)
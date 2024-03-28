# 문제 설명
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
# s는 소문자로만 이루어져 있습니다.

def solution(s):
    answer = ''
    
    alphabet_count = [0] * 26
    for char in s:
        alphabet_count[ord(char) - 97] += 1
    
    for i in range(26):
        if alphabet_count[i] == 1:
            answer += chr(i + 97)
            
    return answer

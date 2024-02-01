# 문제 설명
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

def solution(myString, pat):
    count = 0
    
    for i in range(0, len(myString)-len(pat)+1):
        if myString[i:].startswith(pat):
            count += 1
            
    return count

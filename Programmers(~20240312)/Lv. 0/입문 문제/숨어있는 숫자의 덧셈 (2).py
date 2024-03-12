# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = 0
    
    # 문자열 내 대소문자를 공백으로 치환
    for char in my_string:
        if char.isalpha():
            my_string = my_string.replace(char, ' ')
            
    # 공백을 기준으로 문자열을 나누어 리스트로 저장
    my_string = list(map(int, my_string.split()))
    
    return sum(my_string)

# 문제 설명
# 문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

def solution(strArr):
    answer = 0
    
    # 문자열 길이의 최댓값 구하기
    max_len = 0
    for str in strArr:
        if max_len < len(str):
            max_len = len(str)
    
    # 문자열의 길이를 인덱스로 하는 배열 생성
    len_list = [0] * (max_len + 1)
    
    for  str in strArr:
        len_list[len(str)] += 1

    answer = max(len_list)
    
    return answer

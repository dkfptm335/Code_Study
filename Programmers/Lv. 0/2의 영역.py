# 문제 설명
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

def solution(arr):
    answer = []
    
    # 2가 없는 경우
    if 2 not in arr:
        answer.append(-1)
    
    # 2가 1개 있는 경우
    elif arr.count(2) == 1:
        answer.append(2)
    
    # 2가 2개 이상 있는 경우
    else:
        # 첫 번째 2의 인덱스
        start = arr.index(2)
        
        # 마지막 2의 인덱스
        end = len(arr) - arr[::-1].index(2) - 1
        
        # 2가 모두 포함된 가장 작은 연속된 부분 배열
        answer = arr[start:end+1]
    
    return answer

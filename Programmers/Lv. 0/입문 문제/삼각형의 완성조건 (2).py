def solution(sides):
    answer = 0
    
    # 1. 새로 추가한 변이 가장 긴 변일 때
    # max(sides) < x < sum(sides)
    answer = sum(sides) - max(sides) - 1
    
    # 2. 새로 추가한 변이 가장 긴 변이 아닐 때
    # max(sides) >= x, sum(sides) - max(sides) + x > max(sides)
    # x > max(sides) - sum(sides) + max(sides)
    # 2 * max(sides) - sum(sides) < x <= max(sides)
    answer += sum(sides) - max(sides)
    
    return answer

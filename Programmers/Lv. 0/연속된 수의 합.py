# 문제 설명
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다.
# 두 정수 num과 total이 주어집니다.
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 1 ≤ num ≤ 100
# 0 ≤ total ≤ 1000

def range_sum(start, num):
    return sum(range(start, start + num))

def solution(num, total):
    for i in range(-1000, 1000):
        if range_sum(i, num) == total:
            return list(range(i, i + num))
        
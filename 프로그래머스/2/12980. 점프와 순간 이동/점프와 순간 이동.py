def solution(n):
    # 기능 1: K칸 점프
    # 기능 2: 현재까지 온 거리 * 2 에 해당하는 위치로 순간이동
    
    # 기능 1은 K 만큼의 건전지 사용량
    
    # 이동하려는 거리 N
    
    # N을 2진수로 나타냈을 때, 1의 개수
    return bin(n)[2:].count('1')
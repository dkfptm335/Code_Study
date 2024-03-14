def solution(brown, yellow):
    # 가로 * 세로 == brown + yellow
    mul = brown + yellow
    # 테두리 1줄만 갈색으로 칠해져 있음, 배열의 테두리 개수 구하기
    
    # 가로 >= 세로
    # 1. 약수 순서쌍 구하기
    measures = []
    for i in range(1, int(mul**0.5) + 1):
        if mul % i == 0:
            measures.append(list(reversed([i, mul // i])))
            
    for measure in measures:
        n, m = measure
        if brown == 2*(n+m-2):
            return measure
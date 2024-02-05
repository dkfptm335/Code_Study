def solution(dots):
    # dots: [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    
    # 기울기 비교
    # dots[0], dots[1]
    # dots[0], dots[2]
    # dots[0], dots[3]
    
    # 1. dots[0], dots[1]을 잇는 직선의 기울기 (y2 - y1) / (x2 - x1) 와 dots[2] , dots[3]을 잇는 직선의 기울기 (y4 - y3) / (x4 - x3) 가 같으면 평행
    # 2. dots[0], dots[2]을 잇는 직선의 기울기 (y3 - y1) / (x3 - x1) 와 dots[1] , dots[3]을 잇는 직선의 기울기 (y4 - y2) / (x4 - x2) 가 같으면 평행
    # 3. dots[0], dots[3]을 잇는 직선의 기울기 (y4 - y1) / (x4 - x1) 와 dots[2] , dots[3]을 잇는 직선의 기울기 (y3 - y2) / (x3 - x2) 가 같으면 평행
    
    if (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0]) == (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0]):
        return 1
    elif (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0]) == (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0]):
        return 1
    elif (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0]) == (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0]):
        return 1
    
    return 0

def solution(dots):
    # dots: [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    # if x1 == x2:
    #     return abs(x1-x3) * abs(y1-y2)
    # elif x1 == x3:
    #     return abs(x1-x2) * abs(y1-y3)
    # else:
    #     return abs(x1-x2) * abs(y1-y4)
    
    if dots[0][0] == dots[1][0]:
        return abs(dots[0][0]-dots[2][0]) * abs(dots[0][1]-dots[1][1])
    elif dots[0][0] == dots[2][0]:
        return abs(dots[0][0]-dots[1][0]) * abs(dots[0][1]-dots[2][1])
    else:
        return abs(dots[0][0]-dots[1][0]) * abs(dots[0][1]-dots[3][1])
    
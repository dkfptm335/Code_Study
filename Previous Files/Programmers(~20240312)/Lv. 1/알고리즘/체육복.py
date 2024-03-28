def solution(n, lost, reserve):
    # n: 전체 학생의 수
    # lost: 체육복을 도난당한 학생들의 번호가 담긴 배열
    # reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
    # return: 체육수업을 들을 수 있는 학생의 최댓값
    
    Union = [i for i in range(1, n+1)]
    
    print(Union)
    
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    print(real_lost)
    print(real_reserve)
    
    for student in real_lost:
        if student-1 in real_reserve:
            real_reserve.remove(student-1)
        elif student+1 in real_reserve:
            real_reserve.remove(student+1)
        else:
            Union.remove(student)
    
    print(Union)
    
    return len(Union)

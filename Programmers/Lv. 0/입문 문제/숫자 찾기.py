def solution(num, k):
    list_num = list(map(int, str(num)))
    return list_num.index(k) + 1 if k in list_num else -1

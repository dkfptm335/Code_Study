def solution(phone_number):
    len_star = len(phone_number) - 4
    
    return '*' * len_star + phone_number[-4:]

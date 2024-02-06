def solution(order):
    return str(order).count('3') + str(order).count('6') + str(order).count('9') if '3' in str(order) or '6' in str(order) or '9' in str(order) else 0

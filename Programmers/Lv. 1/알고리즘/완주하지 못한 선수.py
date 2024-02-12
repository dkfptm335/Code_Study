from collections import Counter

def solution(participant, completion):
    count_p = Counter(participant)
    count_c = Counter(completion)
    
    return list((count_p - count_c).keys())[0]

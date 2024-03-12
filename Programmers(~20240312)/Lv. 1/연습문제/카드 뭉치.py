def solution(cards1, cards2, goal):
    
    for word in goal:
        if word in cards1:
            if word == cards1[0]:
                cards1.pop(0)
            else:
                return 'No'
        elif word in cards2:
            if word == cards2[0]:
                cards2.pop(0)
            else:
                return 'No'
        else:
            return 'No'
        
    return 'Yes'

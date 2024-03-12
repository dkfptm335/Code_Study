def solution(keymap, targets):
    # targets에 존재하는 문자들을 keymap의 mapping 최솟값과 딕셔너리로 매핑
    
    # targets에 존재하는 문자 추출
    targets_alpha = []
    alpha_dict = {}
    result = []
    
    for target in targets:
        for char in target:
            if char not in targets_alpha:
                targets_alpha.append(char)
    
    for alpha in targets_alpha:
        location = []
        for key in keymap:
            location.append(key.find(alpha))
            
        if location.count(-1) == len(location):
            alpha_dict[alpha] = -1
        else:
            while -1 in location:
                location.remove(-1)
            alpha_dict[alpha] = min(location) + 1
            
    for target in targets:
        is_possible = True
        tmp = 0
        for char in target:
            tmp += alpha_dict[char]
            if alpha_dict[char] == -1:
                is_possible = False
        
        if is_possible:
            result.append(tmp)
        else:
            result.append(-1)
    
    return result

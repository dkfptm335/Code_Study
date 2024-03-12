def solution(friends, gifts):
    # 인원 별 친구에게 준 선물의 개수를 저장할 딕셔너리
    gift_dict = {name:{} for name in friends}
    for name in gift_dict.keys():
        for friend in friends:
            if name != friend:
                gift_dict[name][friend] = 0
                
    # 다음 달 선물
    next_gift_dict = {name:0 for name in friends}
                
    # 선물 주기
    for gift in gifts:
        sender, receiver = gift.split()
        gift_dict[sender][receiver] += 1
        
    # 선물 지수: 친구들에게 준 선물의 수 - 받은 선물의 수
    # 친구들에게 준 선물의 수
    total_gift_dict = {name:0 for name in friends}
    for key, value in gift_dict.items():
        total_gift_dict[key] = sum(value.values())
        
    # 친구들에게 받은 선물의 수
    total_given_dict = {name:0 for name in friends}
    for name in total_given_dict.keys():
        for key, value in gift_dict.items():
            if not key == value:
                for key1, value1 in value.items():
                    if name == key1:
                        total_given_dict[name] += value1
                        
    # 선물 지수
    gift_score = {name:0 for name in friends}
    for name in gift_score.keys():
        gift_score[name] = total_gift_dict[name] - total_given_dict[name]
        
    # 선물 주고 받은 기록 있는지 확인
    # 중복 없이 두 명의 순서쌍 구하기
    duo = []
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            duo.append([friends[i], friends[j]])
    
    for name1, name2 in duo:
        # 두 사람의 선물 기록 비교
        if gift_dict[name1][name2] > gift_dict[name2][name1]:
            next_gift_dict[name1] += 1
        elif gift_dict[name1][name2] < gift_dict[name2][name1]:
            next_gift_dict[name2] += 1
        else:
            if gift_score[name1] > gift_score[name2]:
                next_gift_dict[name1] += 1
            elif gift_score[name1] < gift_score[name2]:
                next_gift_dict[name2] += 1
    
    # 딕셔너리 상태 출력            
    for key, value in next_gift_dict.items():
        print(f'{key}: {value}')
        
    return max(next_gift_dict.values())

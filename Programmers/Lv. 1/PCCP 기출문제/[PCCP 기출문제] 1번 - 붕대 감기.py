def solution(bandage, health, attacks):
    max_len = attacks[-1][0]

    status = [0] * (max_len+1)
    status[0] = health
    cnt = 0
    
    attack_list = [0]*(max_len+1)
    
    for t, p in attacks:
        attack_list[t] = p
    
    for i in range(1,max_len+1):
        if attack_list[i] != 0: #공격받음
            status[i] = status[i-1] - attack_list[i]
            cnt = 0
            if status[i] <= 0:
                return -1
        else: #공격안함
            status[i] = min(health, status[i-1] + bandage[1])
            cnt += 1
            if cnt == bandage[0]:
                status[i] = min(health, status[i]+bandage[2])
                cnt = 0

    if status[-1] <= 0:
        return -1
    else:
        return status[-1]
    
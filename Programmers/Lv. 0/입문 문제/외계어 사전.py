def solution(spell, dic):
    answer = 0
    
    # dic의 요소마다 spell에 존재하는 알파벳의 개수가 각각 1개인지 확인 후
    # 모두 1개라면 len(spell) == len(dic[i])인지 확인
    # 하나라도 존재한다면 return 1 or 2
    
    for str in dic:
        spell_count = 0
        for sp in spell:
            if str.count(sp) == 1:
                spell_count += 1
        if spell_count == len(spell):
            if len(spell) == len(str):
                return 1
    
    return 2

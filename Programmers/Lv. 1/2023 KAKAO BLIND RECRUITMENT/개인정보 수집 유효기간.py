# 모든 달의 일수는 28일로 고정

def time_convert(date):
    date = date.split('.')
    return int(date[0])*12*28 + int(date[1])*28 + int(date[2])

def solution(today, terms, privacies):
    del_idx = []
    
    today = time_convert(today)
    
    terms_dict = {}
    for term in terms:
        name, period = term.split(' ')
        terms_dict[name] = int(period) * 28
        
    for idx, privacy in enumerate(privacies):
        start, name = privacy.split(' ')
        end = time_convert(start) + terms_dict[name]
        if end <= today:
            del_idx.append(idx+1)
            
    return del_idx

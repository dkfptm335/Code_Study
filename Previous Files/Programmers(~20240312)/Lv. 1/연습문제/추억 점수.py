def solution(name, yearning, photo):
    answer = []
    
    dict_name = {name: yearning for name, yearning in zip(name, yearning)}
    
    for ph in photo:
        sum = 0
        for person in ph:
            if person in dict_name:
                sum += dict_name[person]
        
        answer.append(sum)
    
    return answer

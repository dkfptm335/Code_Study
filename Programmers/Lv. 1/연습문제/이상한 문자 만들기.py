def solution(s):
    word_list = s.split(' ')
    changed_list = []
    
    for word in word_list:
        tmp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        changed_list.append(tmp)
    
    return ' '.join(changed_list)

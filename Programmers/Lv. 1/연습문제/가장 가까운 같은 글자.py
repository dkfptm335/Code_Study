def solution(s):
    answer = []
    
    char_index = {}
    
    for i in range(len(s)):
        if s[i] not in char_index.keys():
            char_index[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i-char_index[s[i]])
            char_index[s[i]] = i
    
    return answer

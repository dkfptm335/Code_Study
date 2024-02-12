def solution(s, skip, index):
    answer = ''
    
    alphabets = [chr(i) for i in range(97, 123)]
    
    for char in skip:
        alphabets.remove(char)
        
    for char in s:
        while alphabets.index(char) + index >= len(alphabets):
            index -= len(alphabets)
        answer += alphabets[alphabets.index(char) + index]
        
    return answer

def solution(s, n):
    answer = ''
    
    # ceaser cipher
    # s: plaintext, n: key
    
    for char in s:
        if char == ' ':
            answer += char
        elif char.isupper():
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
    
    return answer

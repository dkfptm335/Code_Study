def solution(babbling):
    answer = 0
    
    # 조카가 발음할 수 있는 단어: "aya", "ye", "woo", "ma"
    # 배열의 각 요소마다 위의 단어 이외의 문자가 있는지 확인
    # 위의 문자를 ''로 바꾸고, 그 이외의 문자가 있는지 확인
    
    def check_word(word):
        word_list = ["aya", "ye", "woo", "ma"]
        for i in word_list:
            word = word.replace(i, ' ')
        
        if word.strip() == '':
            return True
        else:
            return False
        
    for i in babbling:
        if check_word(i):
            answer += 1
    
    return answer

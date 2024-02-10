def solution(babbling):
    answer = 0
    init = {"aya", "ye", "woo", "ma"}  # 가능한 4가지 단어

    for word in babbling:
        comp = ""  # 비교할 단어
        temp = ""  # 임시 저장할 단어

        for char in word:
            comp += char

            # 연속해서 같은 단어가 나왔을 때 반복문 탈출
            if comp == temp:
                break

            # 4가지 단어가 포함 돼있을 때 현재 단어 임시 저장 후 비교단어 초기화
            if comp in init:
                temp = comp
                comp = ""

        # 비교할 단어가 존재 하지 않을때 카운트
        if comp == "":
            answer += 1

    return answer

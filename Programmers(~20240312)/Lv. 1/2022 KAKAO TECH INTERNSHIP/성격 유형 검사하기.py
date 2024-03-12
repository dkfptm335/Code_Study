def solution(survey, choices):
    result = ''
    
    # MBTI 유형별 점수를 저장할 딕셔너리
    MBTI = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    for i in range(len(survey)):
        # 비동의로 점수를 얻는 유형과 동의로 점수를 얻는 유형 구분
        disagree = survey[i][0]
        agree = survey[i][1]
        
        # 동의 부분
        if choices[i] > 4:
            MBTI[agree] += (choices[i]-4)
        # 비동의 부분
        elif choices[i] < 4:
            MBTI[disagree] += (4-choices[i])
            
    # MBTI 조합하기
    # 1번 지표
    if MBTI['R'] > MBTI['T']:
        result += 'R'
    elif MBTI['R'] == MBTI['T']:
        result += 'R'
    else:
        result += 'T'
        
    # 2번 지표
    if MBTI['C'] > MBTI['F']:
        result += 'C'
    elif MBTI['C'] == MBTI['F']:
        result += 'C'
    else:
        result += 'F'
        
    # 1번 지표
    if MBTI['J'] > MBTI['M']:
        result += 'J'
    elif MBTI['J'] == MBTI['M']:
        result += 'J'
    else:
        result += 'M'
        
    # 1번 지표
    if MBTI['A'] > MBTI['N']:
        result += 'A'
    elif MBTI['A'] == MBTI['N']:
        result += 'A'
    else:
        result += 'N'
        
    return result

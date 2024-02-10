import re

def solution(dartResult):
    regex = re.compile(r'(\d{1,2})([SDT])([*#]?)')
    dart = regex.findall(dartResult)
    score = []
    for i in range(len(dart)):
        if dart[i][1] == 'S':
            score.append(int(dart[i][0]))
        elif dart[i][1] == 'D':
            score.append(int(dart[i][0])**2)
        elif dart[i][1] == 'T':
            score.append(int(dart[i][0])**3)
        if dart[i][2] == '*':
            if i == 0:
                score[i] *= 2
            else:
                score[i-1] *= 2
                score[i] *= 2
        elif dart[i][2] == '#':
            score[i] *= -1
    
    return sum(score)

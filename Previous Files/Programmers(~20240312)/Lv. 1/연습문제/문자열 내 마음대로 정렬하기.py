def swap(a, b):
    return b, a

def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i, len(strings)):
            if strings[i][n] > strings[j][n]:
                strings[i], strings[j] = swap(strings[i], strings[j])
            elif strings[i][n] == strings[j][n]:
                if strings[i] > strings[j]:
                    strings[i], strings[j] = swap(strings[i], strings[j])
    
    return strings

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))
        
    for i in range(len(answer)):
        print(answer[i])
    
    return answer

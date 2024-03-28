# my_str을 n씩 잘라서 배열에 저장

def solution(my_str, n):
    answer = []
    
    for i in range(len(my_str)//n):
        # 일단 n씩 잘라서 배열에 저장한 후, 그만큼 my_str을 갱신
        answer.append(my_str[:n])
        my_str = my_str[n:]
        
    if len(my_str) > 0:
        answer.append(my_str)
    
    return answer

def swap(a, b):
    return b, a

def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    
    # sizes: [[w, h], [w, h], ...]
    
    # 가로가 세로보다 길게 정렬하기
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = swap(sizes[i][0], sizes[i][1])
            
    for i in range(len(sizes)):
        if sizes[i][0] > max_width:
            max_width = sizes[i][0]
        if sizes[i][1] > max_height:
            max_height = sizes[i][1]
    
    answer = max_width * max_height
    
    return answer

def solution(board, h, w):
    # 타겟 색상과 동일한 칸의 개수를 저장할 변수
    same = 0
    
    # board의 가로 및 세로 길이
    n = len(board)
    
    # 타겟 색상 저장
    target_color = board[h][w]
    
    # 위쪽 확인
    if h-1 < 0:
        pass
    else:
        if board[h-1][w] == target_color:
            same+=1
            
    # 아래쪽 확인
    if h+1 > n-1:
        pass
    else:
        if board[h+1][w] == target_color:
            same+=1
    
    # 오른쪽 확인
    if w+1 > n-1:
        pass
    else:
        if board[h][w+1] == target_color:
            same+=1
    
    # 왼쪽 확인
    if w-1 < 0:
        pass
    else:
        if board[h][w-1] == target_color:
            same+=1
            
    return same

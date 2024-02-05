def solution(board):
    safe = 0
    # 1 2 3
    # 4 * 6
    # 7 8 9
    
    # 1부터 8까지 색칠한다는 개념
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                # 1번 위치
                if i-1 >= 0 and j-1 >= 0:
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                # 2번 위치
                if j-1 >= 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                # 3번 위치
                if i+1 < len(board) and j-1 >= 0:
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
                # 4번 위치
                if i-1 >= 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                # 6번 위치
                if i+1 < len(board):
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                # 7번 위치
                if i-1 >= 0 and j+1 < len(board[0]):
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                # 8번 위치
                if j+1 < len(board[0]):
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                # 9번 위치
                if i+1 < len(board) and j+1 < len(board[0]):
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                safe += 1
    
    return safe

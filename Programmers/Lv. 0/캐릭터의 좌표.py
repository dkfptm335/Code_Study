def solution(keyinput, board):
    # 현재 캐릭터의 좌표
    x, y = 0, 0
    
    # x: board[0]
    # y: board[1]
    
    for key in keyinput:
        if key == 'up':
            if y >= (board[1]-1)/2:
                pass
            else:
                y += 1
        elif key == 'down':
            if y <= -(board[1]-1)/2:
                pass
            else:
                y -= 1
                
        elif key == 'left':
            if x <= -(board[0]-1)/2:
                pass
            else:
                x -= 1
        else:
            if x >= (board[0]-1)/2:
                pass
            else:
                x += 1
    
    
    return [x, y]

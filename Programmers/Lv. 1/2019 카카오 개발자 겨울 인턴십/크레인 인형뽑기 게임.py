def solution(board, moves):
    # 터트려진 인형의 개수
    poped = 0
    
    # 행과 열을 바꿔서 스택처럼 사용할 새로운 board
    new_board = []
    
    # 바구니(스택)
    basket = []
    
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[0])):
            tmp.append(board[j][i])
        
        while 0 in tmp:
            tmp.remove(0)
        
        tmp.reverse()
        new_board.append(tmp)
        
    print(new_board)
            
    # ========== 여기까지 OK ==========
    
    for i in range(len(moves)):
        moves[i] -= 1
        
    print(moves)
    
    for move in moves:
        if new_board[move] != []:
            basket.append(new_board[move].pop())
            
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                poped += 2
                
    return poped

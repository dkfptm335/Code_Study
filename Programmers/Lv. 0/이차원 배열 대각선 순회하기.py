# 문제 설명
# 2차원 정수 배열 board와 정수 k가 주어집니다.

# i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.

def solution(board, k):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    
    return answer

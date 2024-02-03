# 문제 설명
# 양의 정수 n이 매개변수로 주어집니다.
# n × n 배열에 1부터 n^2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    # n x n 빈 배열 생성
    answer = [[0] * n for _ in range(n)]
    
    # 값을 채울곳의 인덱스
    x, y = 0, 0
    
    # 오른쪽, 아래, 왼쪽, 위
    direction = 'right'
    
    for num in range(1, n**2 + 1):
        answer[x][y] = num
        
        if direction == 'right':
            if y + 1 >=n or answer[x][y+1] != 0:
                direction = 'down'
                x += 1
            else:
                y += 1
        elif direction == 'down':
            if x + 1 >= n or answer[x+1][y] != 0:
                direction = 'left'
                y -= 1
            else:
                x += 1
        elif direction == 'left':
            if y - 1 < 0 or answer[x][y-1] != 0:
                direction = 'up'
                x -= 1
            else:
                y -= 1
        elif direction == 'up':
            if x - 1 < 0 or answer[x-1][y] != 0:
                direction = 'right'
                y += 1
            else:
                x -= 1
    
    # 배열 출력
    for i in range(len(answer)):
        print(answer[i])
    
    return answer


solution(5) # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]

T = int(input())
test_cases = {}

for i in range(T):
    N = int(input())
    # N by N 배열 생성
    test_cases[i] = [[0] * N for _ in range(N)]

    # 현재 좌표
    x, y = 0, 0
    # 방향
    direction = 'R'
    for j in range(1, N**2 + 1):
        test_cases[i][x][y] = j
        if direction == 'R':
            if y + 1 < N and test_cases[i][x][y + 1] == 0:
                y += 1
            else:
                direction = 'D'
                x += 1
        elif direction == 'D':
            if x + 1 < N and test_cases[i][x + 1][y] == 0:
                x += 1
            else:
                direction = 'L'
                y -= 1
        elif direction == 'L':
            if y - 1 >= 0 and test_cases[i][x][y - 1] == 0:
                y -= 1
            else:
                direction = 'U'
                x -= 1
        elif direction == 'U':
            if x - 1 >= 0 and test_cases[i][x - 1][y] == 0:
                x -= 1
            else:
                direction = 'R'
                y += 1

for i in range(T):
    print(f'#{i + 1}')
    for j in range(len(test_cases[i])):
        print(*test_cases[i][j])
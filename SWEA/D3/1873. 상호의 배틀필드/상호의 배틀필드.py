from collections import deque


def find_tank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '<' or board[i][j] == '>' or board[i][j] == '^' or board[i][j] == 'v':
                return i, j


t = int(input())

for tc in range(1, t + 1):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    n = int(input())
    commands = deque(list(input()))
    x, y = find_tank(grid)

    while commands:
        command = commands.popleft()
        if command == 'U':
            # 전차 방향 변경
            if grid[x][y] != '^':
                grid[x][y] = '^'
            # 한 칸 위가 평지인지 확인
            if x - 1 >= 0:
                if grid[x - 1][y] == '.':
                    # 전차 위로 한 칸 이동
                    grid[x][y], grid[x - 1][y] = grid[x - 1][y], grid[x][y]
                    # 전차 위치 업데이트
                    x -= 1

        elif command == 'D':
            # 전차 방향 변경
            if grid[x][y] != 'v':
                grid[x][y] = 'v'
            # 한 칸 아래가 평지인지 확인
            if x + 1 < len(grid):
                if grid[x + 1][y] == '.':
                    # 전차 아래로 한 칸 이동
                    grid[x][y], grid[x + 1][y] = grid[x + 1][y], grid[x][y]
                    # 전차 위치 업데이트
                    x += 1

        elif command == 'L':
            # 전차 방향 변경
            if grid[x][y] != '<':
                grid[x][y] = '<'
            # 한 칸 왼쪽이 평지인지 확인
            if y - 1 >= 0:
                if grid[x][y - 1] == '.':
                    # 전차 왼쪽으로 한 칸 이동
                    grid[x][y], grid[x][y - 1] = grid[x][y - 1], grid[x][y]
                    # 전차 위치 업데이트
                    y -= 1

        elif command == 'R':
            # 전차 방향 변경
            if grid[x][y] != '>':
                grid[x][y] = '>'
            # 한 칸 오른쪽이 평지인지 확인
            if y + 1 < len(grid[0]):
                if grid[x][y + 1] == '.':
                    # 전차 오른쪽으로 한 칸 이동
                    grid[x][y], grid[x][y + 1] = grid[x][y + 1], grid[x][y]
                    # 전차 위치 업데이트
                    y += 1

        elif command == 'S':
            if grid[x][y] == '^':
                for i in range(x, -1, -1):
                    if grid[i][y] == '*':
                        grid[i][y] = '.'
                        break
                    elif grid[i][y] == '#':
                        break
            elif grid[x][y] == 'v':
                for i in range(x, len(grid)):
                    if grid[i][y] == '*':
                        grid[i][y] = '.'
                        break
                    elif grid[i][y] == '#':
                        break
            elif grid[x][y] == '<':
                for i in range(y, -1, -1):
                    if grid[x][i] == '*':
                        grid[x][i] = '.'
                        break
                    elif grid[x][i] == '#':
                        break
            elif grid[x][y] == '>':
                for i in range(y, len(grid[0])):
                    if grid[x][i] == '*':
                        grid[x][i] = '.'
                        break
                    elif grid[x][i] == '#':
                        break

    print(f'#{tc}', end=' ')
    for i in range(h):
        print(''.join(grid[i]))
        
T = int(input())
test_cases = {}

for i in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    box = True
    vertical = True
    horizontal = True

    # box check (3 by 3)
    for j in range(0, len(sudoku), 3):
        for k in range(0, len(sudoku[j]), 3):
            tmp = []
            for x in range(3):
                for y in range(3):
                    tmp.append(sudoku[j+x][k+y])
            if len(tmp) != len(set(tmp)):
                box = False

    # vertical check
    for j in range(len(sudoku)):
        tmp = []
        for k in range(len(sudoku[j])):
            tmp.append(sudoku[k][j])
        if len(tmp) != len(set(tmp)):
            vertical = False

    # horizontal check:
    for row in sudoku:
        if len(row) != len(set(row)):
            horizontal = False

    test_cases[i] = 1 if box and vertical and horizontal else 0

for i in range(1, T+1):
    print(f'#{i} {test_cases[i]}')
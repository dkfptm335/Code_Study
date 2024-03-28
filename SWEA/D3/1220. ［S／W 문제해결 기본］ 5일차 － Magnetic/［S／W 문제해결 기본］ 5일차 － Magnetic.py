for tc in range(1, 11):
    n = int(input())  # always 100
    board = [list(map(int, input().split())) for _ in range(n)]
    board = list(map(list, zip(*board)))
    count = 0

    for row in board:
        for i in range(len(row)):
            if row[i] != 1:
                row[i] = 0
            else:
                break

        for i in range(len(row) - 1, -1, -1):
            if row[i] != 2:
                row[i] = 0
            else:
                break

        while 0 in row:
            row.remove(0)

        count += len(''.join(map(str, row)).replace('1', ' ').strip().split())

    print(f"#{tc} {count}")

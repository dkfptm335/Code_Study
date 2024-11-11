T = int(input())

for i in range(T):
    N = int(input())
    # N * N 행렬 생성
    answer = [[0 for _ in range(N)] for _ in range(N)]

    x, y, num = 0, 0, 1
    direction = "right"

    while num <= N ** 2:
        answer[x][y] = num
        num += 1

        if direction == "right":
            if y + 1 < N and answer[x][y + 1] == 0:
                y += 1
            else:
                direction = "down"
                x += 1

        elif direction == "down":
            if x + 1 < N and answer[x + 1][y] == 0:
                x += 1
            else:
                direction = "left"
                y -= 1

        elif direction == "left":
            if y - 1 >= 0 and answer[x][y - 1] == 0:
                y -= 1
            else:
                direction = "up"
                x -= 1

        elif direction == "up":
            if x - 1 >= 0 and answer[x - 1][y] == 0:
                x -= 1
            else:
                direction = "right"
                y += 1

    print(f"#{i + 1}")
    for j in range(N):
        print(" ".join(map(str, answer[j])))

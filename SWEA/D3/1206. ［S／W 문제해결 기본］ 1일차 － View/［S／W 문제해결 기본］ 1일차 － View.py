for tc in range(1, 11):
    n = int(input())
    heights = list(map(int, input().strip().split()))
    # 조망권 확보 세대 수
    house = 0

    for i in range(2, n - 2):
        if heights[i] == max([heights[i + j] for j in range(-2, 3)]):
            house += min([heights[i] - heights[i + j] for j in [-2, -1, 1, 2]])

    print(f"#{tc} {house}")
    
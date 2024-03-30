t = int(input())

for tc in range(1, t + 1):
    sizeOfFarm = int(input())
    farm = [list(input()) for _ in range(sizeOfFarm)]
    reversedFarm = list(reversed(farm))

    # 가운데 1줄 더하기
    profit = sum(map(int, farm[sizeOfFarm // 2]))

    for i in range(sizeOfFarm // 2):
        for j in range(sizeOfFarm // 2 - i, (sizeOfFarm // 2) - i + (2 * i + 1)):
            profit += int(farm[i][j]) + int(reversedFarm[i][j])

    print(f"#{tc} {profit}")
    
t = int(input())

for tc in range(1, t + 1):
    d, l, n = map(int, input().strip().split())
    attacked = 0
    attackSum = 0

    for i in range(n):
        attackSum += d * (1 + attacked * l * 0.01)
        attacked += 1

    print(f"#{tc} {int(attackSum)}")
    
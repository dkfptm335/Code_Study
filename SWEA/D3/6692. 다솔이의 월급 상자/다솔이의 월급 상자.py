t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    sum = 0
    for _ in range(n):
        pay = list(map(float, input().split()))
        sum += pay[0] * pay[1]

    print(f"#{tc} {sum}")
    
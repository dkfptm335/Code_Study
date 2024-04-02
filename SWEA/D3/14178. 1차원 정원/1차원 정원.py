t = int(input())

for tc in range(1, t + 1):
    n, d = map(int, input().split())

    sprinkle = n // (2 * d + 1)
    n %= (2 * d + 1)

    if n:
        sprinkle += 1

    print(f"#{tc} {sprinkle}")
    
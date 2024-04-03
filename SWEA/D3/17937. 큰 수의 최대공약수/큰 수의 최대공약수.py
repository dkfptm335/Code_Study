t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    if a == b:
        print(f"#{tc} {a}")
    else:
        print(f"#{tc} {1}")
        
t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    bread = c // min(a, b)

    print(f"#{tc} {bread}")

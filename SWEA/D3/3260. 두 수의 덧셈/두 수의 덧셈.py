t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().strip().split())
    print(f"#{tc} {a + b}")

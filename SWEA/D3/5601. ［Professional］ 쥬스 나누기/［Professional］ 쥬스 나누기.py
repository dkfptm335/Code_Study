t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    juice = [f"1/{n}" for _ in range(n)]
    print(f"#{tc} {' '.join(juice)}")
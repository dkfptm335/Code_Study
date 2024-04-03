t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    l_diff = b - a
    r_diff = c - b

    if l_diff == r_diff:
        print(f"#{tc} 0.0")
    else:
        print(f"#{tc} {abs((r_diff - l_diff) / 2)}")
        
from collections import Counter

t = int(input())

for tc in range(1, t + 1):
    lines = list(map(int, input().split()))
    cnt = Counter(lines)
    target = 0

    if len(cnt) == 1:
        target = list(cnt.keys())[0]

    else:
        target = cnt.most_common(2)[1][0]

    print(f"#{tc} {target}")

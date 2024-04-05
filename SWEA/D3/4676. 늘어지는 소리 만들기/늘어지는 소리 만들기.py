from collections import Counter

t = int(input())

for tc in range(1, t + 1):
    s = list(input().strip())
    dashCount = int(input().strip())
    dashIndex = list(map(int, input().strip().split()))
    cnt = Counter(dashIndex)
    cnt = sorted(dict(cnt).items(), key=lambda x: x[0], reverse=True)

    for idx, dash in cnt:
        if idx != 0:
            tmp = s.pop(idx - 1)
            tmp += '-' * dash
            s.insert(idx - 1, tmp)
        else:
            tmp = '-' * dash
            s.insert(idx, tmp)

    print(f"#{tc} {''.join(s)}")
    
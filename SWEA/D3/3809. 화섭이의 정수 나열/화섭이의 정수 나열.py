t = int(input().strip())
for tc in range(1, t + 1):
    n = int(input().strip())
    value = ''
    while True:
        value += ''.join(map(str, input().split()))
        if len(value) == n:
            break

    target = 0
    while True:
        if str(target) not in value:
            break
        else:
            target += 1

    print(f"#{tc} {target}")

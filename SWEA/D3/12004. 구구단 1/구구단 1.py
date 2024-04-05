T = int(input())

for tc in range(1, T + 1):
    n = int(input().strip())
    is_possible = False
    for a in range(1, 10):
        for b in range(1, 10):
            if a * b == n:
                is_possible = True
                break

        if is_possible:
            break

    if is_possible:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")
        
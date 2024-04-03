t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    s = input()

    is_possible = True

    if n % 2 == 1:
        is_possible = False
    else:
        if s[:n // 2] != s[n // 2:]:
            is_possible = False

    print(f"#{tc} {'Yes' if is_possible else 'No'}")
    
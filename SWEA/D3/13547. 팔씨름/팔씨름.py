t = int(input())

for tc in range(1, t + 1):
    result = input()

    leftMatches = 15 - len(result)
    if leftMatches + result.count('o') >= 8:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")

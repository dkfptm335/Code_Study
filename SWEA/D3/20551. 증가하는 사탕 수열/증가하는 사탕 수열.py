def is_possible(a, b, c):
    if b < 2:
        return False
    elif c < 3:
        return False
    else:
        return True


t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    candies = 0

    if is_possible(a, b, c):
        while b >= c:
            b -= 1
            candies += 1
        while a >= b:
            a -= 1
            candies += 1

        print(f"#{tc} {candies}")
    else:
        print(f"#{tc} -1")

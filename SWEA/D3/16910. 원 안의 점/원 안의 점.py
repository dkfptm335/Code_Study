def isInteger(n):
    if n == int(n):
        return True
    return False


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    countGrid = 0

    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if x ** 2 + y ** 2 <= n ** 2 and isInteger(x) and isInteger(y):
                countGrid += 1

    print(f"#{tc} {countGrid}")

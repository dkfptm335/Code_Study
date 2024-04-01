t = int(input())

for tc in range(1, t + 1):
    number = input().strip()
    lastNum = number[-1]

    isOdd = False
    if int(lastNum) % 2 == 1:
        isOdd = True

    print(f"#{tc} {'Odd' if isOdd else 'Even'}")

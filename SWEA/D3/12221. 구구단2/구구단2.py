T = int(input())


for tc in range(1, T + 1):
    num1, num2 = map(int, input().split())
    result = 0

    if num1 > 9 or num2 > 9:
        result = -1
    else:
        result = num1 * num2

    print(f"#{tc} {result}")
def isSquare(n):
    if n == int(n ** 0.5) ** 2:
        return True
    return False


def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def isSquarePalindrome(n):
    if isPalindrome(n) and isSquare(n) and isPalindrome(int(n ** 0.5)):
        return True
    return False


t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    count = 0

    for number in range(a, b + 1):
        if isSquarePalindrome(number):
            count += 1

    print(f"#{tc} {count}")
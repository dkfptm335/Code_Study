def is_palindrome(s):
    return True if s == s[::-1] else False


t = int(input())

for tc in range(1, t + 1):
    s = input()
    head = s[:len(s) // 2]
    tail = s[len(s) // 2 + 1:]
    isPalOfPal = False

    if is_palindrome(s) and is_palindrome(head) and is_palindrome(tail):
        isPalOfPal = True

    print(f"#{tc} {'YES' if isPalOfPal else 'NO'}")
    
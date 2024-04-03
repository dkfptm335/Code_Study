def is_palindrome(word):
    return word == word[::-1]


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    has_palindrome = False
    cnt = 0
    words = []
    for _ in range(n):
        word = input()
        if is_palindrome(word):
            has_palindrome = True
        else:
            words.append(word)

    for word in words:
        if word[::-1] in words:
            cnt += 1

    if has_palindrome:
        cnt += 1

    print(f"#{tc} {cnt * m}")
    
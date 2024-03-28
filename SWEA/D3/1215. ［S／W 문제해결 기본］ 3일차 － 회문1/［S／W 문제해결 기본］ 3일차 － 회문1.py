def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


for tc in range(1, 11):
    palLength = int(input())
    wordBoard = [list(input()) for _ in range(8)]
    wordBoardTranspose = list(map(list, zip(*wordBoard)))
    count = 0

    for i in range(8):
        for j in range(0, 8 - palLength + 1):
            tmp = ''.join(wordBoard[i][j:j + palLength])
            if isPalindrome(tmp):
                count += 1
            tmp = ''.join(wordBoardTranspose[i][j:j + palLength])
            if isPalindrome(tmp):
                count += 1

    print(f'#{tc} {count}')

alphabets = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())

for tc in range(1, t + 1):
    s = input()
    correctCount = 0

    for i in range(len(s)):
        if s[i] == alphabets[i]:
            correctCount += 1
        else:
            break

    print(f"#{tc} {correctCount}")

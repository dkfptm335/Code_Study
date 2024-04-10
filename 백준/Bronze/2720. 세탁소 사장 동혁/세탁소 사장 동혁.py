import sys

t = int(sys.stdin.readline().strip())
for tc in range(1, t + 1):
    c = int(sys.stdin.readline().strip())
    coins = [c // 25]
    c %= 25
    coins.append(c // 10)
    c %= 10
    coins.append(c // 5)
    c %= 5
    coins.append(c // 1)
    c %= 1

    print(' '.join(list(map(str, coins))))

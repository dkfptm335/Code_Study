def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


t = int(input())

for tc in range(1, t + 1):
    words = input().strip().split()
    l = lcm(len(words[0]), len(words[1]))
    if words[0] * (l // len(words[0])) == words[1] * (l // len(words[1])):
        print(f"#{tc} yes")
    else:
        print(f"#{tc} no")

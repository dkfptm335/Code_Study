t = int(input())

for tc in range(1, t + 1):
    s = input()
    s = s.replace("(|", "*")
    s = s.replace("|)", "*")
    s = s.replace("()", "*")

    ballCount = s.count("*")

    print(f"#{tc} {ballCount}")
    
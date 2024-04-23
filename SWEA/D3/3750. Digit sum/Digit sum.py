answers = []

t = int(input().strip())
for tc in range(1, t + 1):
    n = int(input().strip())

    while len(list(str(n))) != 1:
        n = sum(list(map(int, list(str(n)))))

    answers.append(n)

for tc in range(1, t + 1):
    print(f"#{tc} {answers[tc - 1]}")
    
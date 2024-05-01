t = int(input().strip())
answers = []
for tc in range(t):
    s = list(map(int, list(input().strip())))
    people = 0
    clap = 0

    for i in range(len(s)):
        if s[i] != 0:
            if clap >= i:
                clap += s[i]
            else:
                people += i - clap
                clap += i - clap
                clap += s[i]

    answers.append(people)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")
    
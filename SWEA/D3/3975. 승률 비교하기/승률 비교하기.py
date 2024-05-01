t = int(input().strip())
answers = []
for tc in range(t):
    A, B, C, D = map(int, input().strip().split())
    if (A / B) > (C / D):
        answers.append("ALICE")
    elif (A / B) < (C / D):
        answers.append("BOB")
    else:
        answers.append("DRAW")

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")

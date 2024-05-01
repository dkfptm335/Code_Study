t = int(input().strip())
answers = []
for _ in range(t):
    A, B = map(int, input().strip().split())
    answers.append((A ** 2) // (B ** 2))

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")
    
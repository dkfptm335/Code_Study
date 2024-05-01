primes = [False, False] + [True] * (1000000 - 1)
# 에라토스테네스의 체
for i in range(len(primes)):
    if primes[i]:
        for j in range(2 * i, len(primes), i):
            primes[j] = False

t = int(input().strip())
answers = []
for tc in range(t):
    d, a, b = map(int, input().strip().split())
    count = 0
    for k in range(a, b + 1):
        if primes[k]:
            if str(d) in str(k):
                count += 1

    answers.append(count)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")

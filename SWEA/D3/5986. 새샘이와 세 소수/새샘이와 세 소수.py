a = [False, False] + [True] * (999 - 1)
primes = []
for i in range(len(a)):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, len(a), i):
            a[j] = False

t = int(input().strip())
answers = []
for tc in range(t):
    count = 0
    N = int(input().strip())
    for i in range(len(primes)):
        if primes[i] < N:
            for j in range(i, len(primes)):
                if primes[i] + primes[j] < N:
                    for k in range(j, len(primes)):
                        if primes[i] + primes[j] + primes[k] == N:
                            count += 1

    answers.append(count)

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")

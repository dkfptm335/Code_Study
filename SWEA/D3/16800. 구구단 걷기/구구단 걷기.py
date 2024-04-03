t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    measures = []

    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            measures.append(i + n // i - 2)

    print(f"#{tc} {min(measures)}")
    
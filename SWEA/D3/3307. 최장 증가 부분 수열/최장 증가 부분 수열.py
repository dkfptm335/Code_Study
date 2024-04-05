t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    dp = [1] * len(numbers)

    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    print(f"#{tc} {max(dp)}")
    
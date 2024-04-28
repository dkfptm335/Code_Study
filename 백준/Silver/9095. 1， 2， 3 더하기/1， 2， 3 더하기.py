import sys

t = int(sys.stdin.readline().strip())
answers = []
for tc in range(1, t + 1):
    n = int(sys.stdin.readline().strip())
    dp = [0] * 11
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    answers.append(dp[n - 1])

for answer in answers:
    print(answer)
    
import sys

t = int(sys.stdin.readline().strip())
answers = []
for tc in range(1, t + 1):
    N = int(sys.stdin.readline().strip())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 101):
        dp[i] = dp[i - 2] + dp[i - 3]

    answers.append(dp[N])

for answer in answers:
    print(answer)

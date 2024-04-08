import sys

N, K = map(int, sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(N)]
coins.reverse()
coinCount = 0

for coin in coins:
    coinCount += K // coin
    K %= coin

print(coinCount)

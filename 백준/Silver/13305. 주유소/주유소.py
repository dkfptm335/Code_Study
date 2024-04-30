import sys

N = int(sys.stdin.readline().strip())
roads = list(map(int, sys.stdin.readline().strip().split()))
oilPrices = list(map(int, sys.stdin.readline().strip().split()))[:-1]

# 모든 주유소의 리터당 가격이 1원인 경우
if oilPrices.count(1) == N:
    print(sum(roads))
else:
    curPrice = oilPrices[0]
    priceSum = curPrice * roads[0]
    for i in range(1, len(roads)):
        curPrice = min(curPrice, oilPrices[i])
        priceSum += curPrice * roads[i]

    print(priceSum)

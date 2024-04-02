t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    discount = []

    while len(prices) != 0:
        if int(prices[-1] * 0.75) in prices:
            discount.append(prices.pop())
            prices.remove(int(discount[-1] * 0.75))

    for i in range(len(discount)):
        discount[i] *= 0.75

    discount.sort()
    discount = map(int, discount)

    print(f"#{tc} {' '.join(map(str, discount))}")
    
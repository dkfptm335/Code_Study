T = int(input())
test_cases = {}

for i in range(1, T+1):
    test_cases[i] = []

    # 거슬러 주어야 할 돈의 총 금액
    N = int(input())
    test_cases[i].append(N//50000)
    N %= 50000
    test_cases[i].append(N//10000)
    N %= 10000
    test_cases[i].append(N//5000)
    N %= 5000
    test_cases[i].append(N // 1000)
    N %= 1000
    test_cases[i].append(N // 500)
    N %= 500
    test_cases[i].append(N // 100)
    N %= 100
    test_cases[i].append(N // 50)
    N %= 50
    test_cases[i].append(N // 10)
    N %= 10
    test_cases[i] = map(str, test_cases[i])

for i in range(1,T+1):
    print(f'#{i}')
    print(" ".join(test_cases[i]))
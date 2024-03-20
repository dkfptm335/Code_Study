def sigma(n):
    return n * (n + 1) // 2


T = int(input())
test_cases = {i: 0 for i in range(1, T + 1)}

for i in range(1, T + 1):
    result = input()
    result = result.split('X')

    while '' in result:
        result.remove('')

    test_cases[i] = sum([sigma(len(j)) for j in result])

for i in range(1, T + 1):
    print(test_cases[i])
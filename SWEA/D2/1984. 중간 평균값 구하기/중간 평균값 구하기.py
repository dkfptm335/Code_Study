T = int(input())
test_cases = {i:[] for i in range(1, T+1)}

for i in range(T):
    test_cases[i+1] = list(map(int, input().split()))

for key, value in test_cases.items():
    value.remove(min(value))
    value.remove(max(value))

    value = int(round(sum(value) / len(value), 0))

    print(f'#{key} {value}')
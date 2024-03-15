T = int(input())
test_cases = {i: input() for i in range(1, T+1)}

for key, value in test_cases.items():
    print(value[0]+value[-1])
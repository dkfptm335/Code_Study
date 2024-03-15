T = int(input())
test_cases = {}

for i in range(1, T+1):
    count, deflated = input().split()
    count = int(count)

    result = ''

    for char in deflated:
        result += char * count

    test_cases[i] = result

for key, value in test_cases.items():
    print(value)
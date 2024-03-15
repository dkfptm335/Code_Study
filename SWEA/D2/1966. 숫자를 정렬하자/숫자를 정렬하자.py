T = int(input())
test_cases = {}

for i in range(1, T+1):
    N = int(input())
    test_cases[i] = map(str, sorted([int(x) for x in input().split()]))

for i in range(1, T+1):
    print(f'#{i} {" ".join(test_cases[i])}')

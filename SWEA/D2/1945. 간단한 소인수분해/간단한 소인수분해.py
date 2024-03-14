T = int(input())
test_cases = {i: input() for i in range(1, T+1)}

for i, test_case in test_cases.items():
    a, b, c, d, e = 0, 0, 0, 0, 0
    test_case = int(test_case)

    while test_case % 2 == 0:
        test_case = test_case // 2
        a += 1

    while test_case % 3 == 0:
        test_case = test_case // 3
        b += 1

    while test_case % 5 == 0:
        test_case = test_case // 5
        c += 1

    while test_case % 7 == 0:
        test_case = test_case // 7
        d += 1

    while test_case % 11 == 0:
        test_case = test_case // 11
        e += 1

    print(f'#{i} {a} {b} {c} {d} {e}')
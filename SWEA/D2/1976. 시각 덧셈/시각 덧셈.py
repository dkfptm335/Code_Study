T = int(input())
test_cases = {}

for i in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3, m3 = 0, 0

    m3 += m1 + m2
    if m3 >= 60:
        h3 += 1
        m3 -= 60

    h3 += h1 + h2
    if h3 >= 13:
        h3 -= 12

    test_cases[i] = f'{h3} {m3}'

for i in range(1, T+1):
    print(f'#{i} {test_cases[i]}')
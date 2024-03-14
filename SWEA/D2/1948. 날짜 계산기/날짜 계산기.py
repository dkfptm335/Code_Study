T = int(input())
month_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

for i in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    day1, day2 = 0, 0
    for j in range(1, m1+1):
        if j == m1:
            day1 += d1
        else:
            day1 += month_day[j]

    for j in range(1, m2+1):
        if j == m2:
            day2 += d2
        else:
            day2 += month_day[j]

    result = day2 - day1 + 1
    print(f'#{i+1} {result}')
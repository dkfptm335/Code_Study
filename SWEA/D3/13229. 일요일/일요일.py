days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
daysDict = {}

for idx, value in enumerate(days):
    daysDict[value] = idx + 1

t = int(input())

for tc in range(1, t + 1):
    s = input()
    day = daysDict[s]
    leftDay = 7 - day
    if leftDay == 0:
        leftDay = 7

    print(f"#{tc} {leftDay}")
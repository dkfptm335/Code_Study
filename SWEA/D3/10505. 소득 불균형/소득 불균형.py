T = int(input())


for tc in range(1, T + 1):
    n = int(input())  # 정수의 개수
    incomes = list(map(int, input().split()))  # 소득 리스트
    incomes.sort()
    avg = sum(incomes) / len(incomes)  # 소득 평균
    underAvg = []  # 소득 평균 이하의 사람들

    for income in incomes:
        if income <= avg:
            underAvg.append(income)

    print(f"#{tc} {len(underAvg)}")
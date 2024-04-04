from collections import Counter

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    isPossible = False

    # 최소 숫자 10 (자리수 변동)
    for i in range(2, 11):
        # 자리수 변하면 탈출
        if len(str(n)) != len(str(n * i)):
            break
        else:
            if Counter(list(str(n))) == Counter(list(str(n * i))):
                isPossible = True
                break

    print(f"#{tc} {'possible' if isPossible else 'impossible'}")
    
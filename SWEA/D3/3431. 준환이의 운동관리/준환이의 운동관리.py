T = int(input())

for tc in range(1, T + 1):
    l, u, x = map(int, input().split()) # l분 이상 u분 이하의 운동, 이번 주에 운동한 시간: x분
    demand = 0 # 필요한 운동 시간

    if x < l:
        demand = l - x
    elif x > u:
        demand = -1

    print(f"#{tc} {demand}")
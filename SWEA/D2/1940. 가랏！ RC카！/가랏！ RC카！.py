T = int(input())
test_cases = {i: 0 for i in range(1, T+1)}

for i in range(1, T+1):
    N = int(input())
    commands = [input() for _ in range(N)]

    # 0: 현재 속도 유지
    # 1: 가속
    # 2: 감속

    # 이동 거리
    distance = 0
    # 현재 속도
    speed = 0

    for command in commands:
        if command == '0':
            distance += speed
        elif command.startswith('1'):
            speed += int(command.split()[1])
            distance += speed
        else:
            speed -= int(command.split()[1])
            if speed < 0:
                speed = 0
            distance += speed

    test_cases[i] = distance

for i in range(1, T+1):
    print(f'#{i} {test_cases[i]}')
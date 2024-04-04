for tc in range(1, 11):
    cryptNum = int(input())  # 원본 암호문 뭉치 속 암호문의 개수
    cryptTexts = input().split()  # 원본 암호문 뭉치
    commandNum = int(input())  # 명렁어의 개수
    commands = input().split()  # 명령어
    parsedCommands = []

    tmp = []
    for command in commands:
        if not command.isalpha():
            tmp.append(command)
        else:
            tmp = [command]
            parsedCommands.append(tmp)

    for command in parsedCommands:
        signature = command[0]

        if signature == 'I':
            x, y = int(command[1]), int(command[2])
            s = command[3:]
            cryptTexts = cryptTexts[:x] + s + cryptTexts[x:]

        elif signature == 'D':
            x, y = int(command[1]), int(command[2])
            del cryptTexts[x:x + y]

        else:
            y = int(command[1])
            s = command[2:]
            cryptTexts += s

    print(f"#{tc} {' '.join(cryptTexts[:10])}")
    
for tc in range(1, 11):
    n_crypt = int(input())
    origin_crypt = input().split()
    n_command = int(input())
    commands = input().split("I")[1:]

    for i in range(len(commands)):
        commands[i] = commands[i].strip()

    for command in commands:
        x = int(command.split()[0])
        y = int(command.split()[1])
        s = command.split()[2:]

        origin_crypt = origin_crypt[:x] + s + origin_crypt[x:]

    print(f"#{tc} {' '.join(origin_crypt[:10])}")

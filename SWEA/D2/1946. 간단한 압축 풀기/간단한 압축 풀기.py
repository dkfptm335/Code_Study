T = int(input())
test_cases = {i: [] for i in range(1, T + 1)}

for i in range(1, T + 1):
    N = int(input())
    deflated = [input() for _ in range(N)]
    tmp = ''
    for deflate in deflated:
        for j in range(int(deflate.split(' ')[1])):
            tmp += deflate.split(' ')[0]
            if len(tmp) == 10:
                test_cases[i].append(tmp)
                tmp = ''

    if tmp:
        test_cases[i].append(tmp)

for i in range(1, T + 1):
    print(f'#{i}')
    for j in test_cases[i]:
        print(j)
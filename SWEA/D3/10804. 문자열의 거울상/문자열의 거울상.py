t = int(input())

for tc in range(1, t + 1):
    s = input()
    result = ''

    for char in s:
        if char == 'b':
            result += 'd'
        elif char == 'd':
            result += 'b'
        elif char == 'p':
            result += 'q'
        elif char == 'q':
            result += 'p'

    result = result[::-1]
    print(f'#{tc} {result}')
    
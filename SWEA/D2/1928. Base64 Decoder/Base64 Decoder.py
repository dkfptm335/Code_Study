base = r'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ascii_dict = {idx: value for idx, value in enumerate(base)}
ascii_dict_reverse = {value: key for key, value in ascii_dict.items()}


T = int(input())
test_cases = {i: input() for i in range(1, T + 1)}

for key, value in test_cases.items():
    result = ''

    for char in value:
        ascii_num = ascii_dict_reverse[char]
        binary = bin(ascii_num)[2:]
        result += binary.zfill(6)

    value = result

    # 8자리씩 쪼개기
    result = ''
    for i in range(0, len(value), 8):
        result += value[i:i + 8] + ' '

    result = result.strip().split(' ')
    for idx, value in enumerate(result):
        value = int(value, 2)
        result[idx] = chr(value)

    print(f'#{key} {"".join(result)}')
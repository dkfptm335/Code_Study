# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 입력: 첫 줄에 테스트 케이스의 개수 T가 주어진다.
#      다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
# 출력: #과 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후에 부등호 또는 등호를 출력한다.
#      (1 ≤ 두 수 ≤ 10^4)

T = int(input())
results = []

for i in range(T):
    a, b = map(int, input().split())
    if a > b:
        results.append('>')
    elif a < b:
        results.append('<')
    else:
        results.append('=')

for i in range(len(results)):
    print('#{} {}'.format(i+1, results[i]))
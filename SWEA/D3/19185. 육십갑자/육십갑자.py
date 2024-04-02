# 유클리드 호제법을 이용한 최소공배수 구하기
# 최소공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    LCM = lcm(N,M)                              # N, M의 최소공배수 구하기
    s_list = list(map(str, input().split()))
    t_list = list(map(str, input().split()))
    # 최소공배수만큼 리스트 짜주기
    gapja = []
    for i in range(LCM):
        gapja.append(s_list[i % N] + t_list[i % M])
    # 찾으려는 연도 계산하기
    answer = []
    Q = int(input())
    for _ in range(Q):
        what_year = int(input())
        answer.append(gapja[what_year % LCM -1])
    ans = ' '.join(answer)
    print(f'#{testcase} {ans}')
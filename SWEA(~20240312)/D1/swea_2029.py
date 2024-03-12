T = int(input()) # 테스트 케이스 개수

quotient = []
remainder = []

for i in range(T):
    a, b = map(int, input().split())
    quotient.append(a//b)
    remainder.append(a%b)

for i in range(T):
    print(f'#{i+1} {quotient[i]} {remainder[i]}')
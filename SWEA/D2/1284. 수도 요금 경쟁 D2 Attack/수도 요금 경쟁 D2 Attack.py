# A사: 1리터당 P원
# B사: R리터 이하 Q원, R리터 초과시 1리터당 S원

# 테스트 케이스 개수
T = int(input())
arr = {}

for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q if W <= R else Q + (W - R) * S
    arr[i] = A if A < B else B
    
for i in range(T):
    print(f'#{i+1} {arr[i]}')
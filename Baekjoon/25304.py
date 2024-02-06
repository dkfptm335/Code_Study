# 영수증의 금액 X
# 영수증에 적힌 구매한 물건의 종류의 수 N
# N개의 줄에는 각 물건의 가격과 수량이 주어진다.

X = int(input())
N = int(input())
sum = 0

for _ in range(N):
    price, count = map(int, input().split())
    sum += price * count
    
if X == sum:
    print("Yes")
else:
    print("No")
    
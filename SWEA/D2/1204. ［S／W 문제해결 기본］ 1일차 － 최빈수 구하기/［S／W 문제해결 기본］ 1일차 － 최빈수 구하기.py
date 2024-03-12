from collections import Counter

# 테스트 케이스 T
T = int(input())
arr = {}
mode = {}

for _ in range(T):
    # 테스트 케이스 번호
    test_case = int(input())
    # 테스트 케이스 입력
    arr[test_case] = list(map(int, input().split()))
    # 최빈값 0으로 초기화
    mode[test_case] = 0
    
# 최빈값 구하기
for i in arr:
    c = Counter(arr[i])
    mode[i] = c.most_common(1)[0][0]
    
# 출력
for i in arr:
    print(f'#{i} {mode[i]}')

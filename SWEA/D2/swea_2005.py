# 파스칼의 삼각형

# 테스트 케이스 개수
T = int(input())

# 파스칼의 삼각형을 저장할 리스트
pascal = []

for t in range(T):
    # 파스칼의 삼각형의 크기
    N = int(input())
    
    # 각 테스트 케이스의 파스칼 삼각형 저장
    pascal_t = []
    
    # 각 테스트 케이스의 파스칼 삼각형 구하기, 줄
    for n in range(N):
        
        line = []
        
        # 첫 번째 줄
        if n == 0:
            line.append(1)
            pascal_t.append(line)
        # 두 번째 줄부터
        else:
            for i in range(n+1):
                if i == 0 or i == n:
                    line.append(1)
                else:
                    line.append(pascal_t[n-1][i-1] + pascal_t[n-1][i])
            pascal_t.append(line)
    
    pascal.append(pascal_t)
    
# 출력
for t in range(T):
    print(f'#{t+1}')
    for line in pascal[t]:
        for num in line:
            print(num, end=' ')
        print()
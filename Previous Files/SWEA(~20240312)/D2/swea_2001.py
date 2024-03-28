# 파리 퇴치

def kill_fly(arr, N, M):
    sum = []
    
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            kill = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    kill += arr[k][l]
            sum.append(kill)
            
    return max(sum)
    

# 테스트 케이스 T
T = int(input())
dead_fly = []

for t in range(T):
    N, M = map(int, input().split())
    
    # N x N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 죽인 파리의 수 dead_fly에 추가
    dead_fly.append(kill_fly(arr, N, M))
    
# 결과 출력
for i in range(T):
    print(f'#{i+1} {dead_fly[i]}')
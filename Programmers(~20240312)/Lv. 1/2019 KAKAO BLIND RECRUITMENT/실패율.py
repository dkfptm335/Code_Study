# N: 스테이지 개수
# stages: 사용자가 현재 멈춰있는 스테이지 번호

def solution(N, stages):
    answer = []
    fail = []
    for i in range(1, N+1):
        if len([x for x in stages if x >= i]) == 0:
            fail.append(0)
        else:
            fail.append(stages.count(i) / (len([x for x in stages if x >= i])))
    for i in range(N):
        answer.append(fail.index(max(fail)) + 1)
        fail[fail.index(max(fail))] = -1
    return answer

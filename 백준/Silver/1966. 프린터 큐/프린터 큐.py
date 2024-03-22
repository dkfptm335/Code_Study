import sys
from collections import deque

T = int(sys.stdin.readline())
test_cases = {}

for i in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    # N: 문서의 수, M: 궁금한 문서의 위치
    docs = list(map(int, sys.stdin.readline().split()))
    test_cases[i] = (N, M, docs)

for i in range(1, T+1):
    N, M, docs = test_cases[i]
    docs = deque([(idx, doc) for idx, doc in enumerate(docs)])
    cnt = 0
    while docs:
        if docs[0][1] == max(docs, key=lambda x: x[1])[1]:
            cnt += 1
            idx, doc = docs.popleft()
            if idx == M:
                print(cnt)
                break
        else:
            docs.append(docs.popleft())
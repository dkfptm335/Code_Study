import sys
from collections import Counter


N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

cnt = Counter(N_list)
for i in M_list:
    print(cnt[i], end=' ')
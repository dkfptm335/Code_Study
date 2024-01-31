# P : 000~999

# 1. P > K
# 2. P < K
# 3. P == K

P, K = map(int, input().split())
if P > K:
    print(P-K+1)
elif P < K:
    print(999-K+1+P)
else:
    print(1)
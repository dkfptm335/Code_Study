import sys

N = list(map(int, list(sys.stdin.readline().strip())))

if 0 not in N:
    print(-1)

else:
    N.remove(0)
    N.sort(reverse=True)
    if sum(N) % 3 == 0:
        print(''.join(list(map(str, N))) + '0')
    else:
        print(-1)

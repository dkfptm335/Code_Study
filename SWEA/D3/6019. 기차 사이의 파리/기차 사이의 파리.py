t = int(input().strip())
for tc in range(1, t + 1):
    d, a, b, f = map(int, input().strip().split())
    time = d / (a + b)

    print("#{} {:.6f}".format(tc, time * f))

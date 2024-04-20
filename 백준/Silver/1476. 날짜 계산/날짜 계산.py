import sys

E, S, M = map(int, sys.stdin.readline().strip().split())
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
year, e, s, m = 0, 0, 0, 0
while e != E or s != S or m != M:
    e += 1
    if e == 16:
        e -= 15
    s += 1
    if s == 29:
        s -= 28
    m += 1
    if m == 20:
        m -= 19

    year += 1

print(year)

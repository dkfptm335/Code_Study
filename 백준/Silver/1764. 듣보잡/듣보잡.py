import sys

N, M = map(int, sys.stdin.readline().strip().split())
noHeard = set([sys.stdin.readline().strip() for _ in range(N)])
noSeen = set([sys.stdin.readline().strip() for _ in range(M)])

noHeardAndSeen = noSeen.intersection(noHeard)
noHeardAndSeen = sorted(noHeardAndSeen)
print(len(noHeardAndSeen))
for person in noHeardAndSeen:
    print(person)

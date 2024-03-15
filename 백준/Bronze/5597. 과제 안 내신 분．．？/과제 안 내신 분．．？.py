union = set([i for i in range(1, 31)])
submit = set([int(input()) for _ in range(28)])
print(*sorted(union - submit), sep='\n')
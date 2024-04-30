import sys

polynomials = sys.stdin.readline().strip().split("-")
result = 0
for i in range(len(polynomials)):
    if i == 0:
        result += sum(list(map(int, polynomials[i].split("+"))))
    else:
        result -= sum(list(map(int, polynomials[i].split("+"))))

print(result)

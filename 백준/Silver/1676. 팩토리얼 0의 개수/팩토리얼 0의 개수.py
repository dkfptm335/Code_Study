def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


count = 0

num = factorial(int(input()))

while num % 10 == 0:
    count += 1
    num //= 10

print(count)

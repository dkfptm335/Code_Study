t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    print(f"#{tc} {'Alice' if n % 2 == 0 else 'Bob'}")
    
t = int(input().strip())
for tc in range(1, t + 1):
    n = int(input().strip())
    s1 = (n * (n + 1) // 2)
    s2 = n ** 2
    s3 = n ** 2 + n
    print(f"#{tc} {s1} {s2} {s3}")
    
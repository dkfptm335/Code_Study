result = []

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    tri = [a, b, c]
    max_num = max(tri)
    others = tri.remove(max_num)
    other1, other2 = tri
    if max_num ** 2 == other1 ** 2 + other2 ** 2:
        result.append("right")
    else:
        result.append("wrong")

for r in result:
    print(r)
import sys


def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(sys.stdin.readline())
ranks = []
if n == 0:
    print(0)
else:
    for i in range(n):
        ranks.append(int(sys.stdin.readline()))
    ranks.sort()
    remove_cnt = len(ranks) * 0.15
    remove_cnt = my_round(remove_cnt)

    if remove_cnt == 0:
        print(round(sum(ranks) / len(ranks)))
    else:
        ranks = ranks[remove_cnt:-remove_cnt]
        print(my_round(sum(ranks) / len(ranks)))

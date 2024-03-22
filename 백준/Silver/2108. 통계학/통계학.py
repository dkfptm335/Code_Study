import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(round(sum(nums) / N))
print(nums[N // 2])
if N == 1:
    print(nums[0])
else:
    counter = Counter(nums).most_common(2)
    print(counter[1][0] if counter[0][1] == counter[1][1] else counter[0][0])
print(nums[-1] - nums[0])

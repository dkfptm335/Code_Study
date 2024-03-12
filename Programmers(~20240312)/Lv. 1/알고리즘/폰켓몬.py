def solution(nums):
    half = len(nums) / 2
    nums = list(set(nums))

    return half if half < len(nums) else len(nums)

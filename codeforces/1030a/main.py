def f():
    _ = int(input())
    nums = [int(c) for c in input().split()]
    print(solve(nums))


def solve(nums):
    for x in nums:
        if x != 0:
            return "HARD"
    return "EASY"


f()

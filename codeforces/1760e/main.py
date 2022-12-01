def f():
    T = int(input())
    for _ in range(T):
        _ = input()
        nums = [int(c) for c in input().split()]
        print(solve(nums))


def solve(nums):
    original = count_inversions(nums)
    flip_first_zero = 0
    flip_last_one = 0

    first_zero = -1
    last_one = -1
    for i in range(len(nums)):
        x = nums[i]
        if x == 0:
            if first_zero == -1:
                first_zero = i
        else:
            last_one = i
    if first_zero != -1:
        clone = nums[:]
        clone[first_zero] = 1
        flip_first_zero = count_inversions(clone)
    if last_one != -1:
        clone = nums[:]
        clone[last_one] = 0
        flip_last_one = count_inversions(clone)
    return max(original, flip_first_zero, flip_last_one)


def count_inversions(nums):
    ones = 0
    res = 0
    for x in nums:
        if x == 0:
            res += ones
        else:
            ones += 1
    return res


# print(count_inversions([1, 0, 1, 0]))
# print(count_inversions([0, 1, 0, 0, 1, 0]))
# print(count_inversions([1, 1, 0, 0, 1, 0]))

f()

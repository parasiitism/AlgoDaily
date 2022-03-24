from asyncio import events


def f():
    _ = input()
    nums = [int(x) for x in input().split()]
    odd_cnt = 0
    last_odd_idx = -1
    even_cnt = 0
    last_even_idx = -1
    for i in range(len(nums)):
        x = nums[i]
        if x % 2 == 0:
            even_cnt += 1
            last_even_idx = i
        else:
            odd_cnt += 1
            last_odd_idx = i
    if odd_cnt == 1:
        return last_odd_idx + 1
    return last_even_idx + 1


print(f())

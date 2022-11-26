
def f():
    T = int(input())
    for _ in range(T):
        nums = [int(c) for c in input().split()]
        nums.sort()
        print(nums[1])


f()

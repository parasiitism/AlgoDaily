def mth2last(nums):
    if len(nums) == 0:
        return ''
    n = len(nums)
    m = int(nums[-1])
    if 0 <= n-m-1 and n-m-1 < len(nums):
        return nums[n-m-1]
    return ''


a = [100, 12, 33, 44, 55, 3]
print(mth2last(a))

a = []
print(mth2last(a))

a = [100, 12, 33, 44, 55, 5]
print(mth2last(a))

a = [100, 12, 33, 44, 55, 6]
print(mth2last(a))

print("-----")

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
# read input to know N
t = int(input())
# read N lines
for i in range(t):
    ri = input()  # raw_input() for python2.7
    nums = ri.split()
    result = mth2last(nums)
    print(result)

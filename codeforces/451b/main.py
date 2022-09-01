"""
    1st:
    - sort the arrary
    - find the L and R, and then check if A[:L] + A[L:R:-1] + A[R:] equals to the sorted array

    Time    O(NlogN + N)
    Space   O(N)
"""


def f():
    _ = input()
    nums = [int(c) for c in input().split()]
    solve(nums)


def solve(nums):
    n = len(nums)
    sorted_nums_Key = tuple(sorted(nums))
    if sorted_nums_Key == tuple(nums):
        print("yes")
        print(1, 1)
        return

    j = None
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            if j == None:
                j = i - 1
        else:
            if j != None:
                segment = nums[j:i]
                temp = nums[:j] + segment[::-1] + nums[i:]
                if tuple(temp) == sorted_nums_Key:
                    print("yes")
                    print(j+1, i)
                    return
                print("no")
                return

    if j != None:
        segment = nums[j:n]
        temp = nums[:j] + segment[::-1]
        if tuple(temp) == sorted_nums_Key:
            print("yes")
            print(j+1, n)
            return

    print("no")


def reverrse_subarray_inplace(nums, L, R):
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1


# f()

print("-- approach 1 ended --")

"""
    2nd:
    - actually we can just find out a potential L and R
    - reverse nums[L:R]
    - and check if the result array is sorted

    Time    O(N)
    Space   O(N)
"""


def f():
    _ = input()
    nums = [int(c) for c in input().split()]
    solve(nums)


def solve(nums):
    n = len(nums)
    L = None
    R = n
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            if L == None:
                L = i - 1
        else:
            if L != None:
                R = i
                break

    # segment = nums[L:R]
    # temp = nums[:L] + segment[::-1] + nums[R:]
    reverrse_subarray_inplace(nums, L, R-1)
    print(L, R, nums)
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            print("no")
            return
    print("yes")
    if L == None:
        print(1, 1)
    else:
        print(L+1, R)


# f()

print("-- approach 2 ended --")

"""
    Followup: there are duplicate numbers
    - unlike Q1, the logic to determine a subarray to reverse is a bit trickier. 
    - Consider the example [1, 1, 4, 4, 3, 2], there are potentially 2 subarray we can reverse [1, 1] and [4, 4, 3, 2].
        If we just reverse the first one with the approach in Q1, then we need to find the longest non-decreasing subarray which is a classic DP problem

    Time    O(N)
    Space   O(N) <- the DP array
"""


def f(nums):
    n = len(nums)
    L, R = longest_non_increasing_subarray(nums)
    if L == -1 or R == -1 or nums[L] == nums[R]:
        return (-1, -1, nums)
    reverrse_subarray_inplace(nums, L, R)
    # guard if the result array is not sorted
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            return (-1, -1, nums)
    return (L, R, nums)


def longest_non_increasing_subarray(nums):
    n = len(nums)
    dp = n * [1]  # store the length at every idx
    for i in range(1, n):
        if nums[i-1] >= nums[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    max_length = 0
    L, R = -1, -1
    for i in range(n):
        length = dp[i]
        if length > max_length:
            max_length = length
            L = i - length + 1
            R = i
    return (L, R)


# a = [1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 6]
# print(longest_non_increasing_subarray(a))

print(f([1, 4, 3, 2, 5]))       # (1, 3)
print(f([1, 2, 3, 4, 5]))       # (-1,-1) no need
print(f([1, 1, 4, 3, 2, 5]))    # (2, 4)
print(f([1, 4, 3, 2, 5, 5]))    # (1, 3)
print(f([1, 4, 3, 3, 2, 5]))    # (1, 4)
print("--5--")
print(f([4, 4, 3, 2, 1]))       # (0, 4)
print(f([1, 1, 4, 4, 3, 2]))                    # (2, 5)
print(f([1, 1, 4, 4, 3, 2, 1, 5, 6, 7]))        # (2, 6)
print(f([1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 6]))     # (-1, -1) impossible
print(f([1, 1, 2, 2]))                          # (-1, -1) no need
print("--10--")
print(f([2, 2, 1, 1]))                          # (0, 3)
print(f([1, 2, 1, 2]))                          # (1, 2)
print(f([2, 1, 2, 1]))                          # (-1, -1) impossible

print("-----")


def f1(nums):
    n = len(nums)
    sorted_nums_Key = tuple(sorted(nums))
    if sorted_nums_Key == tuple(nums):
        return (-1, -1)

    L = None
    R = n-1
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            if L == None:
                L = i - 1
        else:
            if L != None:
                R = i - 1
                break
    if L != None:
        segment = nums[L:R+1]
        temp = nums[:L] + segment[::-1] + nums[R+1:]
        if tuple(temp) == sorted_nums_Key:
            return (L, R)

    return (-1, -1)


print(f1([1, 4, 3, 2, 5]))       # (1, 3)
print(f1([1, 2, 3, 4, 5]))       # (-1,-1) no need
print(f1([1, 4, 3, 2]))          # (1, 3)
print(f1([3, 2, 1, 4]))          # (0, 2)
print(f1([99]))                  # (-1,-1)

print("-----")


def f2(nums):
    n = len(nums)
    L = None
    R = n-1
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            if L == None:
                L = i - 1
        else:
            if L != None:
                R = i - 1
                break
    if L == None:
        return (-1, -1)
    reverrse_subarray_inplace(nums, L, R)
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            return (-1, -1)
    return (L, R)


print(f2([1, 4, 3, 2, 5]))       # (1, 3)
print(f2([1, 2, 3, 4, 5]))       # (-1,-1) no need
print(f2([1, 4, 3, 2]))          # (1, 3)
print(f2([3, 2, 1, 4]))          # (0, 2)
print(f2([99]))

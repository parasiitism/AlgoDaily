"""
    The similar classic question is leetcode162: Find Peak Element (find the local maximum)

    Time    O(logN)
    Space   O(1)
"""


def find_local_minimum(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left


a = [1, 2, 3, 1]
print(find_local_minimum(a))  # 0

a = [1, 2, 1, 3, 5, 6, 4]
print(find_local_minimum(a))  # 2

a = [1, 1, 1, 1, 1, 0, 1]
print(find_local_minimum(a))  # 5

a = [1]
print(find_local_minimum(a))  # 0

a = [0, 1]
print(find_local_minimum(a))  # 0

a = [1, 0]
print(find_local_minimum(a))  # 1

a = [10, 2, 3, 4, 5, 6, 8, 1, 4, 6, 1, 4, 9, 7, 1]
print(find_local_minimum(a))  # 1

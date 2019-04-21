def firstMissingPositive(nums):
    """
    sort
    Time    O(nlogn+n)
    Space   O(n)
    """
    if len(nums) == 0:
        return 1

    # if duplicate
    nums = list(set(nums))

    nums = sorted(nums)

    # dont use heap becos it just gurantee the first item is smallest
    # but the rest of the items are not necessarily sorted
    # heapq.heapify(nums)

    # if negative
    for o in nums:
        if o < 1:
            nums = nums[1:]

    j = 0
    for i in range(1, len(nums)+1):
        if nums[j] != i:
            return i
        j += 1
    return j+1


def firstMissingPositive1(nums):
    """
    hashtable
    Time    O(2n)
    Space   O(n+1)

    """
    seen = [False]*(len(nums)+1)
    for num in nums:
        # to avoid negative and out of bound
        if num > 0 and num < len(seen):
            seen[num] = True
    for i in range(1, len(seen)):
        if seen[i] == False:
            return i
    # it means all numbers are continuous, so just return the number of seen
    return len(seen)


"""
    3rd: 
    - put the numbers into correct position in the array
    - iterate the nums again to check if value, i+1, is at index i

    e.g.1.
    0   1   2  3  4
    [1, 3, 2, 3, 5]

    idx = 0:
    nums[0] = 0+1, correct
    
    idx = 1:
    nums[1] != 1+1, incorrect so swap with its value's value

    nums becomes [1, 2, 3, 3, 5]

    idx = 2:
    nums[2] != 2+1, correct

    idx = 3:
    nums[3] != 3+1, should swap. But since nums[2] equals to 3 too, dont swap

    Time    O(n)
    Space   O(1)
    28 ms, faster than 38.37%
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            # check if the number is at correct
            while i+1 != nums[i]:
                targetIdx = nums[i]-1
                # nums[targetIdx] != nums[i] is to avoid infinit loop
                # e.g. if doesnt check....
                # [1, 1, 1, 2, 3]
                # [1, 2, 1, 1, 3]
                # [1, 1, 1, 2, 3]
                # [1, 2, 1, 1, 3]
                # ...
                if targetIdx >= 0 and targetIdx < len(nums) and nums[targetIdx] != nums[i]:
                    nums[i], nums[targetIdx] = nums[targetIdx], nums[i]
                else:
                    break
        # iterate the nums again to check if value, i+1, is at index i
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i+1
        # if all at correct position, return the next number
        return len(nums) + 1


# 3
a = [1, 2, 0]
print(Solution().firstMissingPositive(a))

# 2
a = [3, 4, -1, 1]
print(Solution().firstMissingPositive(a))

# 1
a = [7, 8, 9, 11, 12]
print(Solution().firstMissingPositive(a))

# 2
a = [5, 3, 1]
print(Solution().firstMissingPositive(a))

# 3
a = [5, 4, 1, 2]
print(Solution().firstMissingPositive(a))

print("-----")

# 4
a = [3, 2, 1]
print(Solution().firstMissingPositive(a))

# 1
a = [2, 3]
print(Solution().firstMissingPositive(a))

# 1
a = [2]
print(Solution().firstMissingPositive(a))

# 2
a = [1]
print(Solution().firstMissingPositive(a))

# 1
a = []
print(Solution().firstMissingPositive(a))

print("-----")

# 4
a = [1, 1, 1, 2, 3]
print(Solution().firstMissingPositive(a))

# 4
a = [1, 3, 2, 3, 5]
print(Solution().firstMissingPositive(a))

# 4
a = [1, 3, 2, 3, 5, -1, -10]
print(Solution().firstMissingPositive(a))

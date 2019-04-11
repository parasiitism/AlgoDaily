class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        2nd approach: still binary search but refactor a bit for understanding

        Time	O(logn)
        Space	O(1)
        48 ms, faster than 22.10%
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] < target:
                if target <= nums[right] or nums[mid] > nums[right]:
                    # search right when the pivot is here OR normally nums[mid] < nums[right] and target <= nums[right]
                    left = mid + 1
                else:
                    # otherwise search in another half
                    right = mid - 1
            elif nums[mid] > target:
                if target >= nums[left] or nums[left] > nums[mid]:
                    # search left when the pivot is here OR normally nums[left] < nums[mid] and target >= nums[left]
                    right = mid - 1
                else:
                    # otherwise search in another half
                    left = mid + 1
            else:
                return mid
        return -1


a = [1]
b = a
print(a)
print(b)

a.append(2)
print(a)
print(b)

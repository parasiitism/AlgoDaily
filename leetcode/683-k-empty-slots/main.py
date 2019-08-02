"""
    1st approach: brute force

    Time    O(n^2)
    Space   O(n)
    LTE
"""


class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """
        length = max(bulbs)
        arr = length * [0]
        for i in range(len(bulbs)):
            idx = bulbs[i]-1
            arr[idx] = 1
            lastBulbIdx = -1
            for j in range(len(arr)):
                if arr[j] == 1:
                    if lastBulbIdx > -1:
                        diff = j - lastBulbIdx - 1
                        if diff == k:
                            return i+1
                    lastBulbIdx = j
        return -1


s = Solution()

a = [1, 3, 2]
b = 1
print(s.kEmptySlots(a, b))

a = [1, 4]
b = 2
print(s.kEmptySlots(a, b))

a = [1, 4]
b = 2
print(s.kEmptySlots(a, b))

a = [5, 1, 4, 3, 2]
b = 2
print(s.kEmptySlots(a, b))

print("-----")

"""
    2nd approach: binary search
    - put the numbers into a sorted array
    - every time we put a number into the array we use binary search
    - then we calculate the left_diff and the right_diff
    - if left_diff or right_diff == k, return iteration index

    Time    O(nk)
    Space   O(n)
    1276 ms, faster than 11.70%
"""


class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """
        arr = []
        arr.append(bulbs[0])
        for i in range(1, len(bulbs)):
            # O(logn)
            idx = self.upperBsearch(arr, bulbs[i])
            # but insert() takes O(k)
            arr.insert(idx, bulbs[i])
            if idx == 0:
                diff = arr[1] - arr[0] - 1
                if diff == k:
                    return i+1
            elif idx == len(arr) - 1:
                diff = arr[-1] - arr[-2] - 1
                if diff == k:
                    return i+1
            else:
                leftDiff = arr[idx] - arr[idx-1] - 1
                if leftDiff == k:
                    return i+1
                rightDiff = arr[idx+1] - arr[idx] - 1
                if rightDiff == k:
                    return i+1
        return -1

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()

a = [1, 3, 2]
b = 1
print(s.kEmptySlots(a, b))

a = [1, 4]
b = 2
print(s.kEmptySlots(a, b))

a = [1, 4]
b = 2
print(s.kEmptySlots(a, b))

a = [5, 1, 4, 3, 2]
b = 2
print(s.kEmptySlots(a, b))

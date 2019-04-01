import bisect


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Time  O(n^2)
        Space O(k)
        TLE
        """
        if len(nums) < k or len(nums) == 0 or k <= 0:
            return []
        res = []
        window = []
        temp = 0
        for i in range(k):
            window.append(nums[i])
        temp = self.findMax(window)
        res.append(temp)
        for i in range(k, len(nums)):
            window = window[1:]
            window.append(nums[i])
            temp = self.findMax(window)
            res.append(temp)
        return res

    def findMax(self, nums):
        res = nums[0]
        for num in nums:
            res = max(num, res)
        return res


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Time  O(nlogk)
        Space O(k)
        TLE
        """
        if len(nums) < k or len(nums) == 0 or k <= 0:
            return []
        res = []
        window = sorted(nums[:k])
        res.pop(window[-1])

        for i in range(k, len(nums)):
            # O(logk) to remove the left most item with binary search
            targetToRemove = nums[i-k]
            idxToRemove = bisect.bisect_left(window, targetToRemove)
            window.remove(idxToRemove)
            # O(logk) to add the current item to a correct place in the window
            idxToAdd = bisect.bisect_left(window, nums[i])
            window.insert(idxToAdd, nums[i])
            # last item in the window is the max
            res.append(window[-1])
        return res

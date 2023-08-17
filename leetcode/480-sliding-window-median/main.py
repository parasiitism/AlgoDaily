from sortedcontainers import SortedList
import bisect

"""
    1st approach
    - binary search to 
        - pop the left most item
        - push the right most item to the window
    - therefore to optimize the window sliding

    Time    O(n*2k)
    Space   O(k)
    112 ms, faster than 80.00%
"""


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return 0
        res = []
        window = sorted(nums[:k])
        res.append(self.calMedian(window))

        for i in range(k, len(nums)):
            num = nums[i]
            # Find position where outgoing element should be removed from
            # O(n) remove window.remove(nums[i-k])
            # though it is O(logn) remove but pop(idx) takes O(n)...
            idx = bisect.bisect_left(window, nums[i-k])
            window.pop(idx)

            # Maintain the sorted invariant while inserting incoming element
            idx = bisect.bisect_right(window, num)
            window.insert(idx, num)

            # Find the median
            res.append(self.calMedian(window))

        return res

    def calMedian(self, window):
        half = (len(window)-1)/2
        if len(window) % 2 == 0:
            return (window[half] + window[half+1]) / 2.0
        else:
            return window[half]*1.0


print(Solution().medianSlidingWindow([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 4))

print("----------------------------------------")

"""
    2nd approach
    - similar to 1st approach but use binary search to 
        - pop the left most item
        - push the right most item to the window
    - therefore to optimize the window sliding

    Time    O(n*2k)
    Space   O(k)

    200 ms, faster than 57.24%
"""


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return 0
        medians, window = [], []
        for i in range(len(nums)):
            # find position where outgoing element should be removed from
            if i >= k:
                # O(logk) + O(k) remove with binary search
                idx = bisect.bisect_left(window, nums[i - k])
                window.pop(idx)
            # maintain the sorted invariant while inserting incoming element with binary search
            bisect.insort(window, nums[i])
            # find the medians starting from kth item
            if i+1 >= k:
                half = k/2
                temp = 0.0
                if k % 2 == 0:
                    temp = (window[half-1] + window[half]) / 2.0
                else:
                    temp = float(window[half])
                medians.append(temp)
        return medians


print(Solution().medianSlidingWindow([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 4))

"""
    3rd: bst (in python we can use SortedList)

    Time    O(NlogK)
    Space   O(K)

    200 ms, faster than 57.24%
"""


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        window = SortedList(nums[:k])

        if k % 2 == 1:
            res = [window[k//2]]
            for i in range(k, n):
                window.discard(nums[i-k])
                window.add(nums[i])
                res.append(window[k//2])
            return res
        res = [(window[k//2-1] + window[k//2]) / 2.0]
        for i in range(k, n):
            window.discard(nums[i-k])
            window.add(nums[i])
            res.append((window[k//2-1] + window[k//2]) / 2.0)
        return res

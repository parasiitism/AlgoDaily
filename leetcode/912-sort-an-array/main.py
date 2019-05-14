class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge sort
        # Time  O(nlogn)
        # Space O(n)
        # return self.mergesort(nums)

        # quick sort
        # Time  O(nlogn) -> O(n^2)
        # Space O(logn)
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    # merge sort
    def mergesort(self, nums):
        if len(nums) == 1:
            return nums
        half = len(nums)/2
        left = self.mergesort(nums[:half])
        right = self.mergesort(nums[half:])
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res += left[i:]
        if j < len(right):
            res += right[j:]
        return res

    # quick sort
    def quicksort(self, nums, start, end):
        if start < end:
            pIdx = self.partition(nums, start, end)
            self.quicksort(nums, start, pIdx-1)
            self.quicksort(nums, pIdx+1, end)

    def partition(self, nums, start, end):
        pivot = nums[end]
        pIdx = start
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[end], nums[pIdx] = nums[pIdx], nums[end]
        return pIdx

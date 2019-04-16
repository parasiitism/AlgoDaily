"""
    2nd approach: 2 pointers to merge the arrays like merge sort
	- use 2 pointers to merge the arrays and return merged[half] or (merged[half-1]+merged[half])/2

	Time		O(m+n)
	Space 	O(m+n)
	92 ms, faster than 34.65%
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        if p1 < len(nums1):
            res += nums1[p1:]
        if p2 < len(nums2):
            res += nums2[p2:]
        if len(res) % 2 == 0:
            half = len(res)//2
            left = res[half-1]
            right = res[half]
            return (left + right)/2.0
        half = len(res)//2
        return float(res[half])


a = [1, 3]
b = [2]
print(Solution().findMedianSortedArrays(a, b))

a = [1, 3]
b = [2, 4]
print(Solution().findMedianSortedArrays(a, b))


a = []
b = [1]
print(Solution().findMedianSortedArrays(a, b))

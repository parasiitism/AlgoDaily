"""
    1st approach: hashtable

    Time    O(A+B+max(A,B))
    Space   O(A+B)
    36 ms, faster than 52.13%
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # count occurence
        htA, htB = {}, {}
        for num in nums1:
            if num not in htA:
                htA[num] = 1
            else:
                htA[num] += 1
        for num in nums2:
            if num not in htB:
                htB[num] = 1
            else:
                htB[num] += 1
        # declare hastables for iteration
        largerHt = htA
        smallerHt = htB
        if len(largerHt) < len(smallerHt):
            smallerHt, largerHt = largerHt, smallerHt
        # find the duplicates
        res = []
        for key in largerHt:
            if key in smallerHt:
                occurence = min(largerHt[key], smallerHt[key])
                temp = occurence * [key]
                res += temp
        return res
